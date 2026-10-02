import streamlit as st
from features.actions import Aura
import time


def thinking():
    # making thinking animation
    loading = st.empty()

    frames = [
        "◐ Aura is thinking",
        "◓ Aura is thinking",
        "◑ Aura is thinking",
        "◒ Aura is thinking"
    ]

    for frame in frames:
        loading.write(frame)
        time.sleep(0.5)

    loading.empty()


st.title("Aura Bot")

aura = Aura()
#chat history initialization

if "messages" not in st.session_state:
    st.session_state["messages"] = []

#to show old chats in loop constantly
for message in st.session_state["messages"]:
    with st.chat_message(message['role']):
        st.markdown(message["content"])



if prompt := st.chat_input("Say Something"):
    st.chat_message("user").markdown(prompt)
    #adding chat in history
    st.session_state["messages"].append({"role": 'user', "content": prompt})

#lowering the user prompt
if prompt:
    prompt = prompt.lower()

    #applying condition if user is greeting or not
    if prompt in ['hi','hello','hey','yo','wassup']:
        with st.chat_message("assistant"):
            response = st.write_stream(aura.type_animator(aura.greeting_replies()))
        st.session_state.messages.append({"role": "assistant", "content": response})

    #chcceking user says bye or not
    elif prompt in ['bye','by','see ya']:
        with st.chat_message("assistant"):
            response = st.write_stream(aura.type_animator(aura.farwell_replies()))
        st.session_state.messages.append({"role": "assistant", "content": response})

    # elif 'play' in prompt or 'music' in prompt:
    #     if 'play' in prompt:
    #         prompt = prompt.replace("play","")
    #     elif 'music' in prompt:
    #         prompt = prompt.replace("music","")
    #     thinking()
    #     response = f"Playing {prompt}"
    #     with st.chat_message("assistant"):
    #         st.write(response)
    #     st.session_state.messages.append({"role": "assistant", "content": response})
    #     aura.play_music(prompt)

    else:
        thinking()
        obj1,obj2,flag =  aura.command(prompt)

        if flag:
            if obj1:
                with st.chat_message("assistant"):
                    response = st.write_stream(aura.type_animator(obj1))
                st.session_state.messages.append({"role": "assistant", "content": response})

            if obj2:
                with st.chat_message("assistant"):
                    response = st.write_stream(aura.type_animator(obj2))
                st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                response = st.write_stream(aura.type_animator(aura.success_replies()))
            st.session_state.messages.append({"role": "assistant", "content": response})

        else:
            response = f"Aura: {obj1}"
            with st.chat_message("assistant"):
                st.write_stream(aura.type_animator(response))
            st.session_state.messages.append({"role": "assistant", "content": response})








