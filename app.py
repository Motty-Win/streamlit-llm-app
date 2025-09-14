import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

st.title("LLM日本語チャットデモ")
st.markdown(
    """
### アプリ概要
このWebアプリは、LLM（大規模言語モデル）を活用した日本語チャットサービスです。ラジオボタンで専門家の種類（健康・政治経済）を選択し、質問を入力すると、選択した分野の専門家としてLLMが回答します。

### 操作方法
1. 「専門家の種類を選択してください」から、健康専門家または政治経済専門家を選びます。
2. 「質問を入力」欄に知りたい内容を日本語で入力します。
3. 「送信」ボタンを押すと、LLMが専門的な観点から回答します。
"""
)

# 専門家の種類をラジオボタンで選択
expert_type = st.radio(
    "専門家の種類を選択してください", ("A: 健康専門家", "B: 政治経済専門家")
)

user_input = st.text_input("質問を入力", "")


def get_llm_answer(input_text: str, expert_type: str) -> str:
    """
    入力テキストと専門家タイプを受け取り、LLMの回答を返す関数
    """
    if expert_type.startswith("A"):
        system_message = "あなたは健康に詳しい専門家です。健康に関する質問に専門的な知識で答えてください。"
    elif expert_type.startswith("B"):
        system_message = "あなたは政治経済に詳しい専門家です。政治や経済に関する質問に専門的な知識で答えてください。"
    else:
        system_message = "あなたは日本語の会話に答えるアシスタントです。"
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    result = llm(messages)
    return result.content


if st.button("送信") and user_input:
    answer = get_llm_answer(user_input, expert_type)
    st.write("回答:")
    st.success(answer)
