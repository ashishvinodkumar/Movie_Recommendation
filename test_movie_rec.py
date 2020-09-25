from click.testing import CliRunner
from movie_rec import main


def test_callapi():
  runner = CliRunner()
  result = runner.invoke(main, ['--title', 'Jumanji'])
  assert result.exit_code == 0
  assert 'tt0113497' in result.output
