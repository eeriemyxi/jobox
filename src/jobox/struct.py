import dataclasses
import enum


class ConfigChannelType(enum.Enum):
    ID = 1
    HANDLE = 2


@dataclasses.dataclass(init=True)
class ConfigChannel:
    channel_type: ConfigChannelType
    id: str

    @classmethod
    def from_channel_id(cls, ch: str) -> "ConfigChannel":
        ch = ch.strip()
        is_id = ch[0] == "!"
        return cls(
            id=ch[1:] if is_id else ch,
            channel_type=ConfigChannelType.ID if is_id else ConfigChannelType.HANDLE,
        )
