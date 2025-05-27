# mcp-weather-jp

日本の気象庁APIを使用した天気予報取得のためのMCP（Model Context Protocol）サーバーです。

## 機能

- 気象庁の公式APIから天気予報データを取得
- 地域コードによる地域別天気予報の表示
- MCPサーバーとしての動作とコマンドライン実行の両方に対応

## インストール

```bash
# 依存関係のインストール
uv pip install -e .
```

## 使用方法

### MCPサーバーとして実行

```bash
python weather_JP.py
```

### コマンドライン実行

```bash
# 地域コード一覧を表示
python weather_JP.py --noserver --areas

# 特定地域の天気予報を取得（例：東京都）
python weather_JP.py --noserver --area 130000
```

## 地域コード例

- 130000: 東京都
- 140000: 神奈川県
- 270000: 大阪府
- 010000: 北海道

完全な地域コード一覧は `--areas` オプションで確認できます。

## API

### get_forecast_JP(area_code)
指定した地域コードの天気予報を取得します。

### get_area_json_JP()
気象庁が提供する地域コード一覧（area.json）を取得します。

## ライセンス

MIT