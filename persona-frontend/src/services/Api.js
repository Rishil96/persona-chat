export async function getConversations() {
    const response = await fetch("http://localhost:8000/conversations/");
    const data = await response.json();
    return data;
}
