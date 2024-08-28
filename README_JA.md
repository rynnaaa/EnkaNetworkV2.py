# Enka Network Python

[EN](./README.md) | [TH](./README_TH.md) | JA

https://enka.network/ のAPIラッパーライブラリ

# 🏓 目次

- [💾 インストール](#インストール)
- [✨ 使い方](#使い方)
- [👀 使用例](#使用例)
- [📗 メソッド一覧](#メソッド一覧)
- [📥 レスポンス](#レスポンス)
  - [UID](#uid)
  - [プロフィール](#プロフィール)
- [🚧 データ構造](#データ構造)
  - [プレイヤーオーナー](#プレイヤーオーナー)
  - [Patreonプロフィール](#Patreonプロフィール)
  - [Hoyosプロフィール](#Hoyosプロフィール)
  - [ビルド情報](#ビルド情報)
  - [プロフィール情報](#プロフィール情報)
  - [プレイヤー](#プレイヤー)
    - [名刺](#名刺)
      - [アバターアイコン](#アバターアイコン)
      - [展示キャラクター一覧](#展示キャラクター一覧)
    - [キャラクター](#キャラクター)
      - [アイコン](#アイコン)
      - [命ノ星座](#命ノ星座)
      - [スキル](#スキル)
    - [装備 (聖遺物, 武器)](#装備-聖遺物-武器)
      - [装備情報](#装備情報)
      - [装備ステータス](#装備ステータス)
    - [FIGHT_PROPデータ](#fight_propデータ)
    - [ビルド](#ビルド)
- [🔧 アセット](#アセット)
  - [キャラクター, 命ノ星座, スキル, 名刺](#キャラクター-命ノ星座-スキル-名刺)
    - [NameTextMapHash](#nametextmaphash)
- [🌎 言語のサポート](#言語のサポート)
- [🙋 サポートと質問](#サポートと質問)
- [📄 ライセンス](#ライセンス)

# インストール

```
pip install enkanetworkV2.py
```

# 使い方

```py
import asyncio

from enkanetwork import EnkaNetworkAPI

client = EnkaNetworkAPI()

async def main():
    async with client:
        data = await client.fetch_user(843715177)
        print("=== Player Info ===")
        print(f"Nickname: {data.player.nickname}")
        print(f"Level: {data.player.level}")
        print(f"Icon: {data.player.avatar.icon.url}")
        print(f"Signature: {data.player.signature}")
        print(f"Achievement: {data.player.achievement}")
        print(f"Abyss floor: {data.player.abyss_floor} - {data.player.abyss_room}")
        print(f"Cache timeout: {data.ttl}")

asyncio.run(main())
```

## 出力

```sh
=== Player Info ===
Nickname: mrwan2546
Level: 55
Icon: https://enka.network/ui/UI_AvatarIcon_Kazuha.png
Signature: K A Z U H A M U C H <3
Achievement: 396
Abyss floor: 8 - 3
Cache timeout: 300
```

## 使用例

[example](./example/) を参照

# メソッド一覧

| メソッド名                                | 詳細                                                                                         |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| fetch_user(uid)                     | ユーザーデータの取得 (UID) **(まもなく廃止されます)**                                                 |
| fetch_user_by_uid(uid)              | ユーザーデータの取得 (UID)                                                                               |
| fetch_user_by_username(profile_id)  | ユーザーデータの取得 (プロフィールID) **(Enka.Networkのサブスクライバー向け)**                                |
| fetch_hoyos_by_username(profile_id) | hoyosのユーザーデータの取得 (プロフィールID) **(Enka.Networkのサブスクライバー向け)**                        |
| fetch_builds(profile_id, metaname)  | ビルドデータの取得 (プロフィールID) **(Enka.Networkのサブスクライバー向け)**                               |
| set_language(lang)                  | 言語の設定 <br> [言語のサポート](#言語のサポート) を参照                      |
| update_assets()                     |   |

# レスポンス

## UID

戻り値の型: `EnkaNetworkResponse`
| ラッパー | API | 備考 |
| ---------- | -------------- | ------------------------------------------ |
| player | playerInfo | [プレイヤー](#プレイヤー) を参照 |
| characters | avatarInfoList | [キャラクター](#キャラクター) を参照 |
| profile | - | [プロフィール情報](#プロフィール情報) を参照 |
| owner | owner | [プレイヤーオーナー](#プレイヤーオーナー) を参照 |
| ttl | ttl | |
| uid | uid | |

## プロフィール

戻り値の型: `EnkaNetworkProfileResponse`
| ラッパー | API | 備考 |
| -------- | ---------- | --------------------------------------------------- |
| username | playerInfo | [プレイヤー](#プレイヤー) を参照 |
| profile | profile | [Patreonプロフィール](#Patreonプロフィール) を参照 |
| hoyos | hoyos | [hoyosプロフィール](#hoyosプロフィール) を参照 |

# データ構造

## プレイヤーオーナー

| ラッパー  | API      | 備考                                               |
| -------- | -------- | --------------------------------------------------- |
| hash     | hash     |                                                     |
| username | username | [Tier](#tier) を参照                          |
| profile  | profile  | [Patreonプロフィール](#Patreonプロフィール) を参照 |
| builds   | -        | [ビルド情報](#ビルド情報) を参照   |

## Patreonプロフィール

| ラッパー      | API          | 備考                      |
| ------------ | ------------ | -------------------------- |
| bio          | bio          |                            |
| level        | level        | [Tier](#tier) を参照 |
| profile      | worldLevel   |                            |
| signup_state | signup_state |                            |
| image_url    | image_url    |                            |

## Hoyosプロフィール

| ラッパー      | API          | 備考                                            |
| ------------ | ------------ | ------------------------------------------------ |
| uid_public   | uid_public   |                                                  |
| public       | public       |                                                  |
| verified     | verified     |                                                  |
| player_info  | player_info  | [Patreonプロフィール](#Patreonプロフィール) を参照 |
| signup_state | signup_state |                                                  |
| signup_state | signup_state |                                                  |

## ビルド情報

| ラッパー     | API         | 備考                                  |
| ----------- | ----------- | -------------------------------------- |
| id          | id          |                                        |
| name        | name        |                                        |
| avatar_id   | avatar_id   |                                        |
| avatar_data | avatar_data | [キャラクター](#キャラクター) を参照 |
| order       | order       |                                        |
| live        | live        |                                        |
| settings    | settings    |                                        |
| public      | public      |                                        |

## プロフィール情報

| ラッパー | API | 備考                          |
| ------- | --- | ------------------------------ |
| uid     | -   | ゲーム内UID                    |
| url     | -   | Enka.NetworkへのURL |
| path    | -   | URLのパス                       |

## プレイヤー

| ラッパー            | API                      | 備考                                                |
| ------------------ | ------------------------ | ---------------------------------------------------- |
| nickname           | nickname                 | [名刺](#名刺) を参照                   |
| signature          | signature                |                                                      |
| world_level        | worldLevel               |                                                      |
| achievement        | finishAchievementNum     |                                                      |
| namecard           | namecardId               |                                                      |
| namecards          | showNameCardIdList -> id | [名刺](#名刺) を参照                   |
| abyss_floor        | towerFloorIndex          |                                                      |
| abyss_room         | towerLevelIndex          |                                                      |
| characters_preview | showAvatarInfoList       | [展示キャラクター一覧](#展示キャラクター一覧) を参照 |
| avatar             | profilePicture           | [アバターアイコン](#アバターアイコン) を参照             |

### アバターアイコン

| ラッパー | API      | 備考                                |
| ------- | -------- | ------------------------------------ |
| id      | avatarId |                                      |
| icon    |          | [アイコン情報](#アイコン情報) を参照 |

### 名刺

| ラッパー | API | 備考                                                         |
| ------- | --- | ------------------------------------------------------------- |
| id      | -   | 名刺ID                                                   |
| name    | -   | 名刺の名前                                                 |
| icon    | -   | 名刺アイコン, [アイコン情報](#アイコン情報) を参照           |
| banner  | -   | 名刺のバナー, [アイコン情報](#アイコン情報) を参照         |
| navbar  | -   | 名刺(横長), [アイコン情報](#アイコン情報) を参照 |

### 展示キャラクター一覧

| ラッパー | API | 備考                                             |
| ------- | --- | ------------------------------------------------- |
| id      | -   | アバターID                                         |
| name    | -   | アバター名                                       |
| level   | -   | アバターのレベル                                      |
| icon    | -   | アバターアイコン, [アイコン情報](#アイコン情報) を参照 |

## キャラクター

| ラッパー                 | API                    | 備考                                                  |
| ----------------------- | ---------------------- | ------------------------------------------------------ |
| id                      | avatarId               |                                                        |
| name                    | -                      | アバター名                                              |
| element                 | -                      | [元素タイプ](#元素タイプ) を参照                   |
| rarity                  | -                      | レア度                                                 |
| image                   | -                      | [アイコン](#アイコン) を参照                             |
| xp                      | propMap -> 1001        |                                                        |
| ascension               | propMap -> 1002        |                                                        |
| level                   | propMap -> 4001        |                                                        |
| max_level               | -                      | アバターの最大レベル ( 50/60 等)                          |
| friendship_level        | fetterInfo.level       |                                                        |
| equipments              | equipList              | [装備](#装備-聖遺物-武器) を参照                         |
| stats                   | fightPropMap           | [FIGHT_PROPデータ](#fight_propデータ) を参照            |
| constellations          | talentIdList           | [命ノ星座](#命ノ星座) を参照                             |
| constellations_unlocked | -                      | 解放済みの命ノ星座                                      |
| skill_data              | inherentProudSkillList |                                                        |
| skill_id                | skillDepotId           |                                                        |
| skills                  | -                      |  [スキル](#スキル) を参照                           |

### アイコン

| ラッパー | API | 備考                                                    |
| ------- | --- | -------------------------------------------------------- |
| icon    | -   | アバターアイコン, [アイコン情報](#アイコン情報) を参照        |
| side    | -   | アバターの横向きアイコン, [アイコン情報](#アイコン情報) を参照   |
| banner  | -   | アバターの祈願バナー, [アイコン情報](#アイコン情報) を参照 |

### 命ノ星座

| ラッパー  | API | 備考                      |
| -------- | --- | -------------------------- |
| id       | -   | 命ノ星座ID                  |
| name     | -   | 命ノ星座の名前              |
| icon     | -   | 命ノ星座のアイコンURL        |
| unlocked | -   | 命ノ星座の開放状態           |

### スキル

| ラッパー    | API | 備考                   |
| ---------- | --- | ----------------------- |
| id         | -   | スキルID                 |
| name       | -   | スキル名                 |
| icon       | -   | スキルのアイコンURL       |
| level      | -   | スキルレベル             |
| is_boosted | -   | スキルレベルの増加状態    |

## 装備 (聖遺物, 武器)

| ラッパー    | API                                 | 備考                                            |
| ---------- | ----------------------------------- | ------------------------------------------------ |
| id         | itemId                              |                                                  |
| level      | reliquary -> level, weapon -> level |
| type       | -                                   | 装備タイプ (聖遺物または武器)           |
| refinement | weapon -> affixMap                  |                                                  |
| ascension  | weapon -> promoteLevel              |                                                  |
| detail     | flat                                | [装備情報](#装備情報) を参照 |

### 装備情報

| ラッパー       | API                                 | 備考                                              |
| ------------- | ----------------------------------- | -------------------------------------------------- |
| name          | -                                   | 装備の名前 (聖遺物名 または 武器名)      |
| icon          | icon                                | [アイコン情報](#アイコン情報) を参照               |
| artifact_type | -                                   | [装備タイプ](#装備タイプ) を参照       |
| rarity        | rankLevel                           |                                                    |
| mainstats     | reliquaryMainstat, weaponStats -> 0 | [装備ステータス](#装備ステータス) を参照 |
| substats      | reliquarySubstats, weaponStats -> 1 | [装備ステータス](#装備ステータス) を参照 |

### 装備ステータス

| ラッパー | API     | 備考                          |
| ------- | ------- | ------------------------------ |
| prop_id | prop_id |                                |
| type    | -       | 値のタイプ (整数 または パーセント) |
| name    | -       | FIGHT_PROPの名前             |
| value   | value   |                                |

## FIGHT_PROPデータ

FIGHT_PROPデータでは4つのメソッドから値を取得できます。
| 選択 | 例 | 戻り値 |
|------------------|---------------------------|----------------------------|
| 生のデータを取得 | stats.FIGHT_PROP_HP.value | 15552.306640625 |
| 丸め込んだ数値の取得 | stats.FIGHT_PROP_ATTACK.to_rounded() | 344 |
| パーセントの数値の取得 | stats.FIGHT_PROP_FIRE_ADD_HURT.to_percentage() | 61.5 |
| %付きの数値の取得 | stats.FIGHT_PROP_FIRE_ADD_HURT.to_percentage_symbol() | 61.5% |

## ビルド

`ビルド`のデータは整形されていません。以下のメソッドからデータを取得できます。また、`raw`引数を使うことで完全なデータを得られます。
| 選択 | 例 | 戻り値 |
|------------------|---------------------------|----------------------------|
| アバターIDのリストを取得 | builds.get_avatar_list() | [10000021,10000037,10000025, ...] |
| キャラクターのビルドを取得 | builds.get_character(10000021) | [ビルド情報](#ビルド情報)のリスト |
| アバターIDでビルド情報を取得 | builds.get_character(10000021, 11111111) | [ビルド情報](#ビルド情報) |

# アイコン情報

アイコン情報では2つのメソッドから値を取得できます。
| 選択 | 例 | 戻り値 |
|------------------|---------------------------|--------------------------------|
| ファイル名の取得 | icon.filename | UI_AvatarIcon_Kazuha_Card.png |
| URLの取得 | icon.url | https://enka.network/ui/UI_AvatarIcon_Kazuha_Card.png |

## 装備タイプ

| キー     | 値          |
| ------- | -------------- |
| Flower  | EQUIP_BRACER   |
| Feather | EQUIP_NECKLACE |
| Sands   | EQUIP_SHOES    |
| Goblet  | EQUIP_RING     |
| Circlet | EQUIP_DRESS    |

## 元素タイプ

| キー     | 値    |
| ------- | -------- |
| Cryo    | Ice      |
| Hydro   | Water    |
| Anemo   | Wind     |
| Pyro    | Fire     |
| Geo     | Rock     |
| Electro | Electric |

# アセット

## キャラクター, 命ノ星座, スキル, 名刺

アバターID(avatarId)でキャラクター、命ノ星座、スキル、名刺のアセットを取得できます。

```py
import asyncio

from enkanetwork import Assets

assets = Assets()

async def main():
    # Character
    assets.character(10000046)
    # Constellations
    assets.constellations(2081199193)
    # Skills
    assets.constellations(10462)
    # Namecards
    assets.namecards(210059)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## NameTextMapHash

`NameTextMapHash`はアセット名のテキストが入ったハッシュマップです。`hash_id`から`NameTextMapHash`を以下のように取得できます。

```py
import asyncio

from enkanetwork import Assets

assets = Assets(lang="en") # Set languege before get name (Ex. English)

async def main():
    print(assets.get_hash_map(1940919994)) # Hu tao
    # OR you can get FIGHT_PROP name
    print(assets.get_hash_map("FIGHT_PROP_BASE_ATTACK")) # Base ATK

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## 言語のサポート

| 言語   | コード |
| ---------- | ---- |
| English    | en   |
| русский    | ru   |
| Tiếng Việt | vi   |
| ไทย        | th   |
| português  | pt   |
| 한국어     | kr   |
| 日本語     | jp   |
| 中文       | zh   |
| Indonesian | id   |
| français   | fr   |
| español    | es   |
| deutsch    | de   |
| Taiwan     | cht  |
| Chinese    | chs  |

APIの完全なドキュメントが必要な場合は[EnkaNetwork API Docs](https://github.com/EnkaNetwork/API-docs)を参照してください。


# ライセンス

[MIT License](./LICENSE)
