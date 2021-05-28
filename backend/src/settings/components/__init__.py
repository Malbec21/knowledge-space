from pathlib import PurePath

from decouple import AutoConfig

BASE_DIR = PurePath(__file__).parent.parent.parent.parent

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
config = AutoConfig(
    search_path=BASE_DIR.parent.joinpath("deployment").joinpath("config"),
)
