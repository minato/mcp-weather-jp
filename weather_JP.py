import httpx
from mcp.server.fastmcp import FastMCP
import json
import argparse
import asyncio

# Initialize FastMCP server
mcp = FastMCP("weather_JP")

@mcp.tool()
async def get_forecast_JP(area_code: str) -> str:
    """日本の気象庁APIを使って天気予報を取得する
    Args:
        area_code: 気象庁地域コード（例: 130000 = 東京都）"""
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, timeout=30.0)
            res.raise_for_status()
            data = res.json()
    except Exception as e:
        return f"予報の取得に失敗しました: {e}"
    if not isinstance(data, list) or not data:
        return "予報データがありません"
    forecast = data[0]
    ts = forecast.get("timeSeries", [])
    if not ts:
        return "予報時系列データがありません"
    series = ts[0]
    times = series.get("timeDefines", [])
    areas = series.get("areas", [])
    if not areas:
        return "地域データがありません"
    weathers = areas[0].get("weathers", [])
    lines = [f"{t}: {w}" for t, w in zip(times, weathers)]
    return "\n".join(lines)

@mcp.tool()
async def get_area_json_JP() -> str:
    """気象庁が公開している area.json を返す"""
    url = "https://www.jma.go.jp/bosai/common/const/area.json"
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, timeout=30.0)
            res.raise_for_status()
            data = res.json()
    except Exception as e:
        return f"地域一覧の取得に失敗しました: {e}"
    return json.dumps(data, ensure_ascii=False)

async def main():
    """コマンドライン実行のメイン関数"""
    parser = argparse.ArgumentParser(description="Japanese Weather MCP Server")
    parser.add_argument("--noserver", action="store_true", help="Run as command line tool instead of MCP server")
    parser.add_argument("--area", help="Area code for weather forecast (e.g., 130000 for Tokyo)")
    parser.add_argument("--areas", action="store_true", help="Show available area codes")
    
    args = parser.parse_args()
    
    if args.noserver:
        if args.areas:
            result = await get_area_json_JP()
            print(result)
        elif args.area:
            result = await get_forecast_JP(args.area)
            print(result)
        else:
            print("--noserver requires either --area <code> or --areas")
    else:
        # Initialize and run the MCP server
        mcp.run(transport='stdio')

if __name__ == "__main__":
    asyncio.run(main())
