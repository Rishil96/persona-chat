from typing import List
from fastapi import status, HTTPException
from langchain_core.messages import AIMessage, HumanMessage
from sqlalchemy.orm import Session
from app.enums import Role
from app.db.models import Conversation, Message
from app.llm.registry import get_llm_instance


def send_message(conversation_id: str, user_message: str, model_name: str, db: Session):
    """
    Main chat service function which orchestrates conversation using multiple details and returns the response
    """
    # Step 1: Retrieve conversation using UUID and raise exception in case of conversation not found
    conversation = db.query(Conversation).filter(Conversation.conversation_id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    # Step 2: Structure messages into Langchain acceptable format
    all_messages = conversation.messages
    conversation_history = format_messages(all_messages)
    # Step 3: Get the requested model from registry and add the user message into message history
    llm_instance = get_llm_instance(model_name=model_name)
    conversation_history.append(HumanMessage(user_message))
    llm_response = llm_instance.invoke(conversation_history)
    # Step 4: Make database entry for the latest message
    user_message_obj = Message(conversation_id=conversation.id, role=Role.USER, content=user_message)
    ai_message_obj = Message(conversation_id=conversation.id, role=Role.ASSISTANT, content=llm_response.content)
    db.add(user_message_obj)
    db.add(ai_message_obj)
    db.commit()
    return llm_response.content


def format_messages(messages: List[Message]) -> List[AIMessage | HumanMessage]:
    """
    Helper function to format messages to langchain acceptable format
    """
    formatted_messages = []
    for message in messages:
        if message.role == Role.USER:
            formatted_messages.append(HumanMessage(message.content))
        elif message.role == Role.ASSISTANT:
            formatted_messages.append(AIMessage(message.content))
    return formatted_messages
