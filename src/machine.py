from pydantic import BaseModel, Field

class VirtualMachine(BaseModel):
    name: str
    ram: float
    cpu: float
    os: str = Field(
    ...,
    pattern=(
        r"(?ix)^("

        # Windows short and full forms
        r"(win(dows)?)(\s|-)?(95|98|me|xp|nt|2000|vista|7|8(\.1)?|10|11)|"
        r"(win(dows)?)(\s|-)?server(\s|-)?(2003|2008|2012|2016|2019|2022)|"

        # macOS and mac variants
        r"(mac(\s|-)?os(\s|-)?(x|11|12|13|14)|macos(\s|-)?(mojave|catalina|bigsur|monterey|ventura|sonoma|sequoia))|"

        # Linux distros and flexible formats
        r"(ubuntu(\s|-)?(\d{2}\.\d{2}|v?\d+)?|"
        r"debian(\s|-)?(\d+)?|"
        r"fedora(\s|-)?(\d+)?|"
        r"centos(\s|-)?(\d+)?|"
        r"rhel(\s|-)?(\d+)?|"
        r"arch(\s|-)?linux|"
        r"manjaro|"
        r"alpine(\s|-)?linux|"
        r"kali(\s|-)?linux|"
        r"opensuse|"
        r"gentoo|"
        r"linux(\s|-)?mint|"
        r"pop(\s|-)?os)"

        r")$"
    ),
)
    storage: float
