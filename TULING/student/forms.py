from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100) # 还有min_length参数
    email = forms.EmailField(required=False, label="Your email address") # 设置选填; 自定义字段标注
    # widget参数设定字段的表现逻辑
    # Field类表示验证逻辑
    message = forms.CharField(widget=forms.Textarea)

    # 一次性的自定义表单特定字段验证
    # 强制message字段为四个word以上
    # Django的表单系统会自动查找[clean_字段名]的方法,如果存在,会在执行完指定字段的默认验证逻辑(e.g.CharField)后,
    # 自动调用该方法进行自定义验证
    def clean_message(self):
        # 自定义验证的数据是已经过默认验证逻辑处理过的,所以从self.cleaned_data中获取数据
        # 对于默认验证逻辑检查过的规则,这里不用再检查
        message = self.cleaned_data["message"]
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        # 此处一定要显式返回"清理过的"字段的值,这样才能在自定义的验证方法中修改那个值,
        # 或者转换成其他Python类型
        # 如果没有return, 默认返回None, 这样一来,原来的值就丢失了
        return message
