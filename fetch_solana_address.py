#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.error

def main():
    api_key = os.getenv("FOMO_API_KEY")
    if len(sys.argv) > 1:
        api_key = sys.argv[1]

    url = "https://api.fomoapi.io/v2/users/DexGemsReal"
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            solana_wallet = data.get("wallets", {}).get("solana")
            print(f"Solana Wallet: {solana_wallet}")
            return solana_wallet
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        print(error_body, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching FOMO API user data: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
