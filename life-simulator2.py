import streamlit as st

# 1. 页面基本配置
st.set_page_config(page_title="李伟的童年回忆录", page_icon="⏳", layout="centered")

# 2. 初始化页面状态
if 'page' not in st.session_state:
    st.session_state.page = 1
# 用来记录爸爸在老鳖事件里的选择
if 'turtle_choice' not in st.session_state:
    st.session_state.turtle_choice = None
# 新增：用来记录获得的成就
if 'achievement' not in st.session_state:
    st.session_state.achievement = None


# --- 核心翻页函数 ---
def next_page():
    st.session_state.page += 1


def reset_game():
    st.session_state.page = 1
    st.session_state.turtle_choice = None
    st.session_state.achievement = None  # 重置时清空成就


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
        那是你上小学时的一个大热天。太阳把地面晒得滚烫。
        妈妈早早上班去了，家里只有你和弟弟两个人。
        这时候，你突发奇想：
        **『“去沙河游泳怎么样？”』**

        你心里清楚，妈妈三番五次强调不能下河游泳。你再三考虑后决定：
        """
    )

    # 让老爸做出选择
    choice = st.radio(
        "你的决定是：",
        ("带着弟弟下河游泳（真凉快啊！！！）", "听妈妈的话，坚决不去（安全第一）"),
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
    if st.session_state.turtle_choice == "带着弟弟下河游泳（真凉快啊！！！）":
        # 触发成就 A
        st.session_state.achievement = "🐢 【失而复得的老鳖】"
        
        st.warning("🌊 你和弟弟一头扎进了凉爽的河水里，那叫一个痛快！")
        st.info(
            "✨ 【意外收获】：你在游泳的时候，脚底踩到一个硬硬的东西，伸手一抓——居然逮到了一只大老鳖！你和弟弟兴奋得手舞足蹈。")
        st.error(
            """
            😱 【乐极生悲】：你们的老鳖被你们同乡给骗走了，晌午你们一身泥进家门，就看到妈妈黑着脸站在院子里，拿起柳条向你们打去。

            **结局：** 你和弟弟被罚跪在堂屋的地上，膝盖生疼，屁股上被打的净是红印子。厨房里飘来炖饭菜的香味，但妈妈正在气头上，发话『今天谁也别想吃饭！』。
            你摸着咕噜咕噜叫的肚子，感觉膝盖跪的生疼。
            """
        )

    # 走向结局 B：没去游泳
    else:
        # 触发成就 B
        st.session_state.achievement = "🍉 【西瓜大王】"
        
        st.success("🏠 你摇了摇头，拉着弟弟回家在院子里的阴凉处写作业。")
        st.info(
            """
            **结局：**
            中午妈妈下班回来，看到你们乖乖在家里，高兴地摸了摸你们的头。晚饭做了一桌子你爱吃的家常菜，又切了个大西瓜，这一天平平安安地过去了。

            不过，深夜躺在床上的你，听着窗外的蛙鸣，偶尔也会想：如果白天带弟弟去了，我们会不会抓到什么好玩的东西呢？（比如……一只老鳖？）
            """
        )

    st.write("")
    st.button("继续前进 ⏭️", on_click=next_page)


# ================== 第四页：温情尾声 ==================
elif st.session_state.page == 4:
    st.balloons()  # 满屏飘气球祝福
    st.title("❤️ 尾声：致最棒的老爸")
    
    # 精准对齐的成就展示
    if st.session_state.achievement:
        st.success(f"🏅 本次模拟中，你达成了专属成就：**{st.session_state.achievement}**")
    
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