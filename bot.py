import os
import time
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Cargar claves desde .env
load_dotenv()
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# Inicializar conexión con Alpaca
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

# Configuraciones
SYMBOL = "AAPL"
TAKE_PROFIT_PERCENT = 0.05     # 5% arriba para vender
BUY_DISCOUNT_PERCENT = 0.02    # 2% abajo para comprar
MAX_LEVERAGE = 2.0             # Apalancamiento permitido
MAX_SHARES_PER_TRADE = 10      # Límite para control

def get_equity():
    """Obtiene el capital total de la cuenta"""
    return float(api.get_account().equity)

def get_price(symbol):
    """Obtiene el precio actual del símbolo"""
    return api.get_latest_trade(symbol).price

def get_position(symbol):
    """Devuelve la cantidad actual de acciones que tienes"""
    try:
        return int(api.get_position(symbol).qty)
    except tradeapi.rest.APIError:
        return 0  # No hay posición

def cancel_all_orders():
    """Cancela todas las órdenes pendientes"""
    api.cancel_all_orders()

def place_limit_buy(symbol, qty, price):
    """Coloca orden límite de compra"""
    print(f"🟢 Colocando orden de COMPRA {qty} {symbol} a ${price}")
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side="buy",
        type="limit",
        time_in_force="gtc",
        limit_price=price
    )

def place_limit_sell(symbol, qty, price):
    """Coloca orden límite de venta"""
    print(f"🔴 Colocando orden de VENTA {qty} {symbol} a ${price}")
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side="sell",
        type="limit",
        time_in_force="gtc",
        limit_price=price
    )

def calculate_position_size(price, equity, leverage):
    """Calcula cuántas acciones se pueden comprar respetando el apalancamiento"""
    max_value = equity * leverage
    max_shares = int(max_value // price)
    return max_shares

def run_bot():
    print("🚀 Bot iniciado (con control de apalancamiento)")

    while True:
        try:
            market_price = get_price(SYMBOL)
            position_qty = get_position(SYMBOL)

            cancel_all_orders()  # Limpia órdenes anteriores

            if position_qty > 0:
                # Si ya tienes acciones → coloca orden de venta con ganancia
                entry_price = float(api.get_position(SYMBOL).avg_entry_price)
                target_price = round(entry_price * (1 + TAKE_PROFIT_PERCENT), 2)
                place_limit_sell(SYMBOL, position_qty, target_price)
                print(f"💼 Tienes {position_qty} acciones a ${entry_price}, vendiendo a ${target_price}")

            else:
                # Si NO tienes acciones → calcula cuánto puedes comprar
                equity = get_equity()
                max_qty = calculate_position_size(market_price, equity, MAX_LEVERAGE)

                if max_qty < 1:
                    print("⚠️ No hay suficiente margen para operar con este apalancamiento.")
                else:
                    qty_to_buy = min(max_qty, MAX_SHARES_PER_TRADE)
                    buy_price = round(market_price * (1 - BUY_DISCOUNT_PERCENT), 2)
                    place_limit_buy(SYMBOL, qty_to_buy, buy_price)
                    print(f"🕒 Orden de compra colocada a ${buy_price} para {qty_to_buy} acciones")

        except Exception as e:
            print("❌ Error:", e)

        time.sleep(60)  # Espera 1 minuto antes de repetir

if __name__ == "__main__":
    run_bot()