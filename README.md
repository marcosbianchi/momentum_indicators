Python3 script para obtener los valores de MFI y RSI dentro del periodo de 15 min. de una lista de pares crytpo (ej. BTCUSDT)

Si el RSI se encuentra en el rango de 35, el indicador se muestra en verde 

Utiliza las librerias binance.client y talib para tomar los datos de los pares crypto y calcular los indicadores.

Se debe hacer un export de las variables de entorno binance_api y binance_secret con los datos de la cuenta en Binance

TODO:
  - cargar los pares de cryptos desde un archivo
  - hacer que el script se ejecute en loop
