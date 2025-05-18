# 🤖 Trading Bot con Apalancamiento (Alpaca Paper Trading)

Este bot compra acciones automáticamente cuando bajan un 2% desde el precio actual y vende con una ganancia del 5%. Incluye control de apalancamiento y protección ante margen insuficiente.

---

## 🛠 Requisitos

- Python 3.8 o superior
- Cuenta en [Alpaca](https://alpaca.markets/) (modo paper trading)
- Claves API de Alpaca

---

## 🚀 Instalación

```bash
git clone https://github.com/tu_usuario/trading-bot-apalancado.git
cd trading-bot-apalancado
pip install -r requirements.txt
````

1. Copia el archivo `.env.example` a `.env` y coloca tus credenciales de Alpaca:

```
APCA_API_KEY_ID=tu_api_key
APCA_API_SECRET_KEY=tu_secret_key
APCA_API_BASE_URL=https://paper-api.alpaca.markets
```

2. Activa un entorno virtual (opcional pero recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux / macOS
.\venv\Scripts\activate   # Windows
```

3. Ejecuta el bot:

```bash
python bot.py
```

## ⚙️ Parámetros configurables

| Parámetro              | Descripción                      | Valor por defecto |
| ---------------------- | -------------------------------- | ------------- |
| `SYMBOL`               | Símbolo de la acción a operar    | AAPL          |
| `TAKE_PROFIT_PERCENT`  | % de ganancia para vender        | 0.05 (5%)     |
| `BUY_DISCOUNT_PERCENT` | % de descuento para comprar      | 0.02 (2%)     |
| `MAX_LEVERAGE`         | Apalancamiento máximo permitido  | 2.0           |
| `MAX_SHARES_PER_TRADE` | Máximo de acciones por operación | 10            |

---

## 🧠 Cómo funciona

* Si no tienes acciones, el bot coloca una orden límite de compra a un precio 2% menor al mercado.
* Si tienes acciones, coloca una orden límite de venta a un 5% por encima del precio de compra.
* Controla cuánto puedes comprar basado en tu equity y apalancamiento máximo.
* Protege contra operaciones cuando no tienes margen suficiente.
* Cancela órdenes pendientes antes de colocar nuevas.

---

## 🛡️ Licencia

Este proyecto está licenciado bajo la licencia MIT.  
Puedes usar, modificar y distribuir el código libremente, incluso con fines comerciales, siempre que mantengas el aviso de copyright y la licencia.  
[Más info aquí](https://opensource.org/licenses/MIT)

---

## 📚 Recursos

* [Alpaca API docs](https://alpaca.markets/docs/api-documentation/)
* [Python alpaca-trade-api](https://github.com/alpacahq/alpaca-trade-api-python)
* [Python dotenv](https://pypi.org/project/python-dotenv/)

---

## 🚀 Contacto

Para dudas o sugerencias, contáctame [aquí](mailto:deangelis.antonio122@gmail.com) o crea un issue en el repo.

---

¡Gracias por usar el bot! 🦜📈