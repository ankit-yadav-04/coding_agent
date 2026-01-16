from client.llm_client import LLMClient
import asyncio


async def main():
    print("--------  Hello from coding-agent! --------\n\n")

    client = LLMClient()
    messages = [{"role": "user", "content": "what's up buddy!"}]
    async for event in client.chat_completion(messages, True):
        print(event)

    print("\n\n---------  Done  -----------")


if __name__ == "__main__":
    asyncio.run(main())
