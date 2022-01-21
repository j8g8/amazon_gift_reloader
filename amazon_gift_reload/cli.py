"""Console script for amazon_gift_reload."""
import argparse
import sys
import getpass

from amazon_gift_reload import AmazonGiftReloader


def main():
    """Console script for amazon_gift_reload."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--amount", type=float, default="0.5", help="dollar value of single reload"
    )
    parser.add_argument("--quantity", type=int, default=1, help="number of reloads")
    parser.add_argument("--email", required=True, help="amazon email login")
    parser.add_argument("--password", help="optional amazon login password")
    parser.add_argument(
        "--force", nargs="?", type=bool, const=True, default=False, help="skip approval"
    )

    args = parser.parse_args()

    if args.password == None:
        args.password = getpass.getpass("Enter %s password: " % args.email)

    print(
        f"[!] ready to reload ${args.amount} x {args.quantity} times for a total of ${args.amount * args.quantity} for amazon user {args.email}!"
    )
    user_acceptance = "y" if args.force else input("[?] apply reload? (y/n) ")
    if user_acceptance == "y":
        reloader = AmazonGiftReloader(
            args.amount, args.quantity, args.email, args.password
        )
        reloader.run()
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
