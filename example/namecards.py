import asyncio

from enkanetwork import EnkaNetworkAPI

client = EnkaNetworkAPI(lang="th")

async def main():
    async with client:
        data = await client.fetch_user(843715177)
        print("=== Namecard main ===")
        print(f"ID: {data.player.namecard.id}")
        print(f"Name: {data.player.namecard.name}")
        print(f"Banner URL: {data.player.namecard.banner.url}")
        print(f"Navbar URL: {data.player.namecard.navbar.url}")
        print(f"Icon URL: {data.player.namecard.icon.url}")
        print("\n")
        print("=== List Namecard ===")
        for namecard in data.player.namecards:
            print(f"ID: {namecard.id}")
            print(f"Name: {namecard.name}")
            print(f"Banner URL: {namecard.banner.url}")
            print(f"Navbar URL: {namecard.navbar.url}")
            print(f"Icon URL: {namecard.icon.url}")
            print("-"*18)

asyncio.run(main())