import streamlit as st

# 1. 页面基本配置
st.set_page_config(page_title="李伟的童年回忆录", page_icon="⏳", layout="centered")

# 2. 初始化页码状态（用来控制当前停留在哪一页）
if 'page' not in st.session_state:
    st.session_state.page = 1
# 用来记录爸爸在老鳖事件里的选择
if 'turtle_choice' not in st.session_state:
    st.session_state.turtle_choice = None


# --- 核心翻页函数 ---
def next_page():
    st.session_state.page += 1


def reset_game():
    st.session_state.page = 1
    st.session_state.turtle_choice = None


# ================== 第一页：封面 ==================
if st.session_state.page == 1:
    st.title("👨‍👦 李伟的专属人生模拟器")
    st.write("")
    st.write("爸，欢迎来到由我用 Python 为你定制的时光机。")
    st.write("接下来的每一页，都是属于你的回忆。点击下方按钮，开启故事吧！")
    st.write("")
    st.button("🚀 开启回忆之旅", on_click=next_page)


# ================== 第二页：故事背景与抉择 ==================
elif st.session_state.page == 2:
    st.header("📅 第一章： 沈丘的夏天很热")
    st.write(
        """
        那是你大约 10 岁时的一个大热天。太阳把地面晒得滚烫，大人们都在午睡。

        这时候，弟弟悄悄拉了拉你的衣角，眼神里闪烁着兴奋的光芒：
        **『哥，天太热了，咱管不管去沙河游泳哎？』**

        你心里清楚，妈妈三番五次强调不能下河游泳。作为哥哥，你决定：
        """
    )

    # 让老爸做出选择
    choice = st.radio(
        "你的决定是：",
        ("跟着弟弟下河游泳（真凉快啊！！！）", "听妈妈的话，坚决不去（安全第一）"),
        key="temp_choice"
    )

    # 确认选择并进入下一页
    if st.button("确认选择，走向明天 ⏭️"):
        st.session_state.turtle_choice = choice
        next_page()


# ================== 第三页：根据选择展示结果 ==================
elif st.session_state.page == 3:
    st.header("🍃 第二章：抉择的后续")

    # 走向结局 A：游泳了
    if st.session_state.turtle_choice == "跟着弟弟下河游泳（真凉快啊！！！）":
        st.warning("🌊 你和弟弟一头扎进了凉爽的河水里，那叫一个痛快！")
        st.info(
            "✨ 【意外收获】：你在摸鱼的时候，脚底踩到一个硬硬的东西，伸手一抓——居然逮到了一只大老鳖！你和弟弟兴奋得手舞足蹈。")
        st.error(
            """
            😱 【乐极生悲】：你们的老鳖被你们同乡给骗走了，傍晚你们刚进家门，就看到妈妈黑着脸站在院子里，不等你反应就劈脸扇了过来

            **结局：** 你和弟弟被罚跪在堂屋的地上，膝盖生疼。厨房里飘来炖饭菜的香味，但妈妈正在气头上，发话『今天谁也别想吃饭！』。
            你摸着咕噜咕噜叫的肚子，感觉膝盖跪的生疼
            """
        )

    # 走向结局 B：没去游泳
    else:
        st.success("🏠 你摇了摇头，拉着弟弟回家在院子里的阴凉处写作业。")
        st.info(
            """
            **结局：**
            傍晚妈妈下班回来，看到你们乖乖在家里，高兴地摸了摸你们的头。晚饭做了一桌子你爱吃的家常菜，又切了个大西瓜，这一天平平安安地过去了。

            不过，深夜躺在床上的你，听着窗外的蛙鸣，偶尔也会想：如果白天跟弟弟去了，我们会不会抓到什么好玩的东西呢？（比如……一只老鳖？）
            """
        )

    st.write("")
    st.button("继续前进 ⏭️", on_click=next_page)


# ================== 第四页：温情尾声 ==================
elif st.session_state.page == 4:
    st.balloons()  # 满屏飘气球祝福
    st.title("❤️ 尾声：致最棒的老爸")
    st.write(
        """
        时光荏苒，当年的小男孩现在已经成为了一位父亲。

        谢谢你陪伴我成长。

        **祝老爸父亲节快乐，身体健康，天天开心！✨**
        """
    )
    st.write("")
    if st.button("🔄 重新体验一次"):
        reset_game()