import pytest

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass



# при выполнении команды PYTEST TEST.PY --SETUP-SHOW то мы увидим след запись:
# test.py
#       SETUP    C prepare_faces
#         SETUP    F print_smiling_faces
#         SETUP    F very_important_fixture
#         test.py::TestPrintSmilingFaces::test_first_smiling_faces (fixtures used: prepare_faces, print_smiling_faces, very_important_fixture).
#         TEARDOWN F very_important_fixture
#         TEARDOWN F print_smiling_faces
#         SETUP    F print_smiling_faces
#         test.py::TestPrintSmilingFaces::test_second_smiling_faces (fixtures used: prepare_faces, print_smiling_faces).
#         TEARDOWN F print_smiling_faces
#       TEARDOWN C prepare_faces