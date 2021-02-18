PRINTER_NAME="BlackHole"
PRINTER_COMMENT="Test printer for printing nothing to nowhere"
PAUSE_PRINTER=false

ENABLE_PRINTER='-E'
if [ $PAUSE_PRINTER == true ]
then
  ENABLE_PRINTER=''
fi

echo "Adding printer '$PRINTER_NAME'"
lpadmin $DISABLE_PRINTER -p "$PRINTER_NAME" $ENABLE_PRINTER -D "$PRINTER_COMMENT" -v file:/dev/null
lpstat -s
