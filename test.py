import pyupbit


access = "DHrlGZKLgEbnFbcbzGSCNuf4Jq2CxWqxwyx097bx"          # 본인 값으로 변경
secret = "MUZDjdxCiZB18kvXuTbMnUckUMMMx1qHLs9YEcWI"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-EOS"))     # KRW-EOS 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(pyupbit.get_tickers(fiat="KRW-CBK"))