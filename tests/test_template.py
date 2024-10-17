import subprocess
from pathlib import Path

from cookiecutter.main import cookiecutter


TEMPLATE_DIR = Path(__file__).parent.parent


def test_dev():
    assert TEMPLATE_DIR.exists()


def test_can_create_template(tmpdir):
    context = {
        "project_name": "mytestproj",
        "project_slug": "mytestproj",
        "package_name": "mytestproj",
        "project_short_description": "Test Python Project",
        "year": "2024",
        "version": "0.0.1",
        "github_username": "testuser",
        "full_name": "Test Person",
        "email": "example@example.com",
        "pypi_username": "testuser"
    }
    # Genearte the template in our temp dir.
    cookiecutter(
        str(TEMPLATE_DIR),
        no_input=True,
        extra_context=context,
        output_dir=str(tmpdir),
    )
    # Sanity checks to make sure the temp dir looks right.
    project_dir = tmpdir / "mytestproj"
    assert project_dir.exists()
    assert (project_dir / "README.md").exists()
    assert (project_dir / "pyproject.toml").exists()
    assert (project_dir / "tests").exists()
    assert (project_dir / "tests" / "__init__.py").exists()
    assert (project_dir / ".github" / "workflows" / "run-tests.yml").exists()
    expected_dirs = [
        project_dir / "src",
        project_dir / "tests",
        project_dir / "docs",
    ]
    # Verify that all expected directories exist
    for directory in expected_dirs:
        assert directory.isdir(), f"Expected directory {directory} does not exist."

    # Now let's try to actually init a venv.
    result = subprocess.run(['uv', 'sync', '--all-extras', '--dev'], cwd=project_dir)
    assert result.returncode == 0, f"Failed to initialize virtual environment: {result.stderr}"
    # Check we can run our checker and have it pass.
    checker_result = subprocess.run(['uv', 'run', 'poe', 'check'], cwd=project_dir)
    assert checker_result.returncode == 0, f"Failed to run checker: {checker_result.stderr}"
