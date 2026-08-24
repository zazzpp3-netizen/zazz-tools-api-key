import os
import json
import time
import requests
from datetime import datetime
from urllib.parse import quote

RED = "\033[91m"
WHITE = "\033[97m"
GRAY = "\033[90m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

API_URL = "https://zazzynz.vercel.app/api/bot/generate"
WA_NUMBER = "62882008584519"
KEY_FILE = "api_keys.json"


def clear():
    os.system("clear")


def now():
    return datetime.now().strftime("%H:%M:%S")


def line():
    print(GRAY + "─" * 52 + RESET)


def header(title):
    print()
    print(RED + "╭" + "─" * 50 + "╮" + RESET)
    print(RED + "│" + RESET + " " * 18 + title.center(32) + RED + "│" + RESET)
    print(RED + "╰" + "─" * 50 + "╯" + RESET)
    print()


def banner():
    print(RED + r"""
╭────────────────────────────────────────────────────╮
│                                                    │
│                    Z A Z Z                         │
│                API MANAGEMENT                      │
│                                                    │
╰────────────────────────────────────────────────────╯
""" + RESET)


def pause():
    input(
        GRAY +
        "\n  [ Enter ] Kembali" +
        RESET
    )


def mask_key(key):
    if len(key) <= 8:
        return "*" * len(key)

    return key[:4] + "*" * (len(key) - 8) + key[-4:]


def load_keys():
    if not os.path.exists(KEY_FILE):
        return []

    try:
        with open(KEY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data if isinstance(data, list) else []

    except:
        return []


def save_keys(keys):
    with open(KEY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            keys,
            f,
            indent=4,
            ensure_ascii=False
        )


def progress(text):
    print()
    print("  " + text)

    total = 24

    for i in range(total + 1):
        filled = "█" * i
        empty = "░" * (total - i)

        percent = int((i / total) * 100)

        print(
            "\r  " +
            RED +
            filled +
            GRAY +
            empty +
            RESET +
            f" {percent:3d}%",
            end="",
            flush=True
        )

        time.sleep(0.025)

    print()


def check_server():
    try:
        response = requests.get(
            API_URL,
            timeout=5
        )

        return True

    except:
        return False


def request_api():
    clear()
    banner()
    header("REQUEST API")

    print(
        "  " +
        GRAY +
        "Server  " +
        RESET +
        "zazzynz.vercel.app"
    )

    print(
        "  " +
        GRAY +
        "Time    " +
        RESET +
        now()
    )

    line()

    api_key = input(
        "\n  " +
        WHITE +
        "API Key  " +
        RESET +
        "→ "
    ).strip()

    if not api_key:
        print(
            "\n  " +
            RED +
            "API Key tidak boleh kosong." +
            RESET
        )
        pause()
        return

    print()
    print(
        "  " +
        GRAY +
        "Key     " +
        RESET +
        mask_key(api_key)
    )

    progress("Connecting to API")

    try:
        response = requests.post(
            API_URL,
            headers={
                "x-api-key": api_key
            },
            timeout=30
        )

        status = response.status_code

        print()

        if status == 200:
            status_text = GREEN + "200 OK" + RESET

        elif status == 400:
            status_text = YELLOW + "400 BAD REQUEST" + RESET

        elif status == 401:
            status_text = RED + "401 UNAUTHORIZED" + RESET

        elif status == 403:
            status_text = RED + "403 FORBIDDEN" + RESET

        elif status == 409:
            status_text = YELLOW + "409 CONFLICT" + RESET

        elif status == 429:
            status_text = YELLOW + "429 TOO MANY REQUESTS" + RESET

        elif status >= 500:
            status_text = RED + f"{status} SERVER ERROR" + RESET

        else:
            status_text = YELLOW + f"{status} HTTP" + RESET

        print(
            RED +
            "╭──────────────────────────────────────────────────╮" +
            RESET
        )

        print(
            "│  STATUS   " +
            status_text +
            " " * max(0, 37 - len(str(status_text))) +
            "│"
        )

        print(
            RED +
            "╰──────────────────────────────────────────────────╯" +
            RESET
        )

        print()

        try:
            data = response.json()

            print(
                "  " +
                WHITE +
                "Response" +
                RESET
            )

            line()

            print(
                json.dumps(
                    data,
                    indent=4,
                    ensure_ascii=False
                )
            )

        except ValueError:
            print(
                "  " +
                response.text
            )

    except requests.exceptions.Timeout:
        print(
            "\n  " +
            RED +
            "Request timeout." +
            RESET
        )

    except requests.exceptions.ConnectionError:
        print(
            "\n  " +
            RED +
            "Tidak dapat terhubung ke server." +
            RESET
        )

    except requests.exceptions.RequestException as e:
        print(
            "\n  " +
            RED +
            "Request gagal." +
            RESET
        )

        print(
            "  " +
            GRAY +
            str(e) +
            RESET
        )

    pause()


def buy_api():
    clear()
    banner()
    header("BUY API KEY")

    print(
        RED +
        "  BASIC" +
        RESET
    )

    print("  Masa aktif : 7 Hari")
    print("  Limit      : 15 Request / Hari")
    print("  Harga      : Rp25.000")

    print()

    print(
        RED +
        "  PREMIUM" +
        RESET
    )

    print("  Masa aktif : 30 Hari")
    print("  Limit      : 20 Request / Hari")
    print("  Harga      : Rp100.000")

    line()

    choice = input(
        "\n  Pilih paket [1/2] → "
    ).strip()

    if choice == "1":
        package = "API Key Basic"
        price = "Rp25.000"

    elif choice == "2":
        package = "API Key Premium"
        price = "Rp100.000"

    else:
        print(
            "\n  " +
            RED +
            "Pilihan tidak tersedia." +
            RESET
        )
        pause()
        return

    message = (
        "Halo Zazz, saya ingin membeli "
        + package +
        " dengan harga "
        + price +
        "."
    )

    print()

    print(
        "  Paket  → " +
        WHITE +
        package +
        RESET
    )

    print(
        "  Harga  → " +
        WHITE +
        price +
        RESET
    )

    print(
        "  Order  → " +
        GREEN +
        "WhatsApp" +
        RESET
    )

    print()

    encoded = quote(message)

    os.system(
        "termux-open-url "
        + '"https://wa.me/'
        + WA_NUMBER
        + "?text="
        + encoded +
        '"'
    )

    pause()


def save_api():
    clear()
    banner()
    header("SAVE API KEY")

    key = input(
        "  API Key → "
    ).strip()

    if not key:
        print(
            "\n  " +
            RED +
            "API Key tidak boleh kosong." +
            RESET
        )
        pause()
        return

    keys = load_keys()

    if key in keys:
        print(
            "\n  " +
            YELLOW +
            "API Key sudah tersimpan." +
            RESET
        )
        pause()
        return

    keys.append(key)
    save_keys(keys)

    print(
        "\n  " +
        GREEN +
        "API Key berhasil disimpan." +
        RESET
    )

    print(
        "  " +
        GRAY +
        mask_key(key) +
        RESET
    )

    pause()


def show_keys():
    clear()
    banner()
    header("MY API KEYS")

    keys = load_keys()

    if not keys:
        print(
            "  " +
            GRAY +
            "Belum ada API Key tersimpan." +
            RESET
        )

        pause()
        return

    for i, key in enumerate(keys, 1):
        print(
            "  " +
            RED +
            f"{i:02d}" +
            RESET +
            "  " +
            mask_key(key)
        )

    print()
    line()

    print(
        "  Total key : " +
        WHITE +
        str(len(keys)) +
        RESET
    )

    pause()


def delete_api():
    clear()
    banner()
    header("DELETE API KEY")

    keys = load_keys()

    if not keys:
        print(
            "  " +
            GRAY +
            "Tidak ada API Key tersimpan." +
            RESET
        )

        pause()
        return

    for i, key in enumerate(keys, 1):
        print(
            "  " +
            RED +
            f"{i:02d}" +
            RESET +
            "  " +
            mask_key(key)
        )

    print()

    choice = input(
        "  Nomor → "
    ).strip()

    try:
        index = int(choice) - 1

        if index < 0 or index >= len(keys):
            raise ValueError

    except ValueError:
        print(
            "\n  " +
            RED +
            "Nomor tidak valid." +
            RESET
        )

        pause()
        return

    keys.pop(index)
    save_keys(keys)

    print(
        "\n  " +
        GREEN +
        "API Key berhasil dihapus." +
        RESET
    )

    pause()


def main():
    while True:
        clear()
        banner()

        server = check_server()

        if server:
            status = (
                GREEN +
                "● ONLINE" +
                RESET
            )
        else:
            status = (
                RED +
                "● OFFLINE" +
                RESET
            )

        print(
            "  Status   " +
            status
        )

        print(
            "  Server   " +
            GRAY +
            "zazzynz.vercel.app" +
            RESET
        )

        print(
            "  Time     " +
            GRAY +
            now() +
            RESET
        )

        line()

        print()
        print(
            "  " +
            RED +
            "01" +
            RESET +
            "  Request API"
        )

        print(
            "      " +
            GRAY +
            "Generate menggunakan API Key" +
            RESET
        )

        print()
        print(
            "  " +
            RED +
            "02" +
            RESET +
            "  Buy API Key"
        )

        print(
            "      " +
            GRAY +
            "Lihat paket dan lakukan order" +
            RESET
        )

        print()
        print(
            "  " +
            RED +
            "03" +
            RESET +
            "  Save API Key"
        )

        print(
            "      " +
            GRAY +
            "Simpan key secara lokal" +
            RESET
        )

        print()
        print(
            "  " +
            RED +
            "04" +
            RESET +
            "  My API Keys"
        )

        print(
            "      " +
            GRAY +
            "Lihat key yang tersimpan" +
            RESET
        )

        print()
        print(
            "  " +
            RED +
            "05" +
            RESET +
            "  Delete API Key"
        )

        print(
            "      " +
            GRAY +
            "Hapus key dari perangkat" +
            RESET
        )

        print()
        print(
            "  " +
            GRAY +
            "00" +
            RESET +
            "  Exit"
        )

        print()
        line()

        choice = input(
            "\n  " +
            RED +
            "zazz@termux ~ $ " +
            RESET
        ).strip()

        if choice in ("1", "01"):
            request_api()

        elif choice in ("2", "02"):
            buy_api()

        elif choice in ("3", "03"):
            save_api()

        elif choice in ("4", "04"):
            show_keys()

        elif choice in ("5", "05"):
            delete_api()

        elif choice in ("0", "00"):
            clear()

            print(
                RED +
                "\n  Zazz Tools closed.\n" +
                RESET
            )

            break

        else:
            print(
                "\n  " +
                RED +
                "Command tidak ditemukan." +
                RESET
            )

            time.sleep(0.8)


if __name__ == "__main__":
    main()