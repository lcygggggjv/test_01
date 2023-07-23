
import datetime

concurrent = datetime.datetime.now()
formtime = concurrent.strftime("%Y-%m-%d %H:%M:%S")


a = f'''李春雨发起微信转账:200w
发送时间: {formtime}
接收人：赵悦琪
接收入口: loading....
'''


print(a)
