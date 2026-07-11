#!/usr/bin/env python3

def encode_teint(value:int):
    if value < 0:
        raise ValueError("The value must be >= 0")
    if value > 999999:
        raise ValueError("The value must be <= 999999")
    v0 = (value ^ 54321) + 13579
    v1 = (value + 13579) ^ 54321
    return v0, v1

def decode_teint(v0:int):
    return (v0 - 13579) ^ 54321

def main():
    print("TEInt Calculator")
    s=input("Enter the number of Bills: ").strip()
    value=int(s)
    v0,v1=encode_teint(value)
    print(f"\nValue: {value}")
    print(f"v0: {v0}")
    print(f"v1: {v1}")
    print("\nJSON:")
    print(f'"coin":{{"v0":{v0},"v1":{v1}}}')
    print(f"\nVerification (decode v0): {decode_teint(v0)}")

if __name__=="__main__":
    main()
