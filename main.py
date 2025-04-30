from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

from jx3api import JX3API

api = JX3API(token="123", ticket="")


@register("jx3helper", "Ming", "一个简单的 剑网三 机器人", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("日常")
    async def helloworld(self, event: AstrMessageEvent):
        """这是一个 hello world 指令"""  # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        result = api.active_calendar(server="梦江南")

        logger.info(event.message_chain)
        yield event.plain_result(f"【时间】${result['date']} 星期${result['week']}\n"
                                 f"【大战】${result['war']}"
                                 f"【战场】${result['battle']}"
                                 f""
                                 f""
                                 f""
                                 f"")  # 发送一条纯文本消息

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""

