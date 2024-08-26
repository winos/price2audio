import numpy as np
import yfinance as yf
from pydub import AudioSegment
from pydub.generators import Sine
import matplotlib.pyplot as plt

# Descargar datos históricos del EUR/USD usando yfinance
# EUR/USD está representado como 'EURUSD=X' en yfinance
data = yf.download('EURUSD=X', start='2023-08-01', end='2023-08-25', interval='1h')

# Utilizar los precios de cierre
prices = data['Close'].tolist()

# Normalizar precios para obtener un rango entre 0 y 1
normalized_prices = (np.array(prices) - min(prices)) / (max(prices) - min(prices))

# Parámetros de generación de audio
base_freq = 440  # Frecuencia base en Hz (La estándar)
duration_ms = 500  # Duración de cada tono en milisegundos
volume = -10  # Volumen en decibelios

audio = AudioSegment.silent(duration=0)

# Generar un tono para cada punto de precio
for price in normalized_prices:
    freq = base_freq + (price * 1000)  # Modificar frecuencia según el precio
    sine_wave = Sine(freq).to_audio_segment(duration=duration_ms, volume=volume)
    audio += sine_wave

# Guardar el archivo de audio
audio.export("eurusd_price_structure_yfinance.wav", format="wav")

# Graficar los precios para referencia visual
plt.plot(prices, label="Precio EUR/USD")
plt.xlabel("Tiempo")
plt.ylabel("Precio")
plt.title("Estructura de Precios EUR/USD (yfinance)")
plt.legend()
plt.show()
