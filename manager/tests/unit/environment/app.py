from unittest import expectedFailure, TestCase, main
from environment.app import AppEnvironment
from environment.reader import EnvironmentReader


class MockEnv(EnvironmentReader):
    variables: dict[str, str]

    def __init__(self) -> None:
        self.variables = {}

    def has(self, variable: str) -> bool:
        return variable in self.variables

    def get(self, variable: str) -> str:
        if not self.has(variable):
            raise Exception("Missing tested variable")

        return self.variables[variable]


class TestAppEnvironment(TestCase):
    def init_env(self) -> AppEnvironment:
        return AppEnvironment(self.processEnv, self.fileEnv)

    def setUp(self) -> None:
        self.processEnv = MockEnv()
        self.fileEnv = MockEnv()

    def test_should_read_from_the_process_environment_first(self) -> None:
        self.processEnv.variables["MINIO_BUCKET"] = "my-special-test-bucket"
        self.fileEnv.variables["MINIO_BUCKET"] = "not-my-special-test-bucket"
        env = self.init_env()
        self.assertEqual(env.MINIO_BUCKET, "my-special-test-bucket")

    def test_should_read_from_the_file_second(self) -> None:
        self.fileEnv.variables["MINIO_BUCKET"] = "my-special-test-bucket"
        env = self.init_env()
        self.assertEqual(env.MINIO_BUCKET, "my-special-test-bucket")

    def test_should_use_local_default_when_variable_is_undefined(self) -> None:
        env = self.init_env()
        self.assertEqual(env.MINIO_BUCKET, "micro-file-manager-contents")

    def test_should_combine_process_and_file_and_defaults(self) -> None:
        self.processEnv.variables["MINIO_BUCKET"] = "my-special-test-bucket"
        self.fileEnv.variables["MINIO_BUCKET"] = "not-my-special-test-bucket"
        self.fileEnv.variables["MINIO_HOST"] = "my.test.host.com"
        env = self.init_env()
        self.assertEqual(env.MINIO_BUCKET, "my-special-test-bucket")
        self.assertEqual(env.MINIO_HOST, "my.test.host.com")
        self.assertEqual(env.MINIO_USER, "minio")

    def test_should_accept_true_string_value_for_boolean_variables(self) -> None:
        self.processEnv.variables["MINIO_USE_TLS"] = "True"
        env = self.init_env()
        self.assertEqual(env.MINIO_USE_TLS, True)

    def test_should_accept_false_string_value_for_boolean_variables(self) -> None:
        self.processEnv.variables["MINIO_USE_TLS"] = "False"
        env = self.init_env()
        self.assertEqual(env.MINIO_USE_TLS, False)

    def test_should_accept_1_string_value_for_boolean_variables(self) -> None:
        self.processEnv.variables["MINIO_USE_TLS"] = "1"
        env = self.init_env()
        self.assertEqual(env.MINIO_USE_TLS, True)

    def test_should_accept_0_string_value_for_boolean_variables(self) -> None:
        self.processEnv.variables["MINIO_USE_TLS"] = "0"
        env = self.init_env()
        self.assertEqual(env.MINIO_USE_TLS, False)

    @expectedFailure
    def test_should_fail_when_value_for_boolean_variable_is_invalid(self) -> None:
        self.processEnv.variables["MINIO_USE_TLS"] = "No"
        self.init_env()

    def test_should_convert_numeric_strings_to_int_variables(self) -> None:
        self.processEnv.variables["MINIO_PORT"] = "123"
        env = self.init_env()
        self.assertEqual(env.MINIO_PORT, 123)

    @expectedFailure
    def test_should_fail_when_value_for_int_variable_is_invalid(self) -> None:
        self.processEnv.variables["MINIO_PORT"] = "that port over there"
        self.init_env()


if __name__ == "__main__":
    main()
