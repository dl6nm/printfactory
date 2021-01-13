$PrinterName = "BlackHole"
$PrinterComment = "Onlineprinters test printer for printing nothing to nowhere"
$PrinterPortName = "BlackHole"
$PrinterDriverName = "Generic / Text Only"

$PausePrinter = 1
$erroraction = 'silentlycontinue'

$PrinterPort = Get-PrinterPort -Name $PrinterPortName -erroraction $erroraction
if (-not $PrinterPort) {
    Write-Host "Adding printer port '$PrinterPortName'"
    Add-PrinterPort -Name $PrinterPortName
}

$PrinterDriver = Get-PrinterDriver -Name $PrinterDriverName -erroraction $erroraction
if (-not $PrinterDriver) {
    Write-Host "Adding printer driver '$PrinterDriverName'"
    Add-PrinterDriver -Name $PrinterDriverName
}

$Printer = Get-Printer -Name $PrinterName -erroraction $erroraction
if (-not $Printer) {
    Write-Host "Adding printer '$PrinterName'"
    Add-Printer -Name $PrinterName -Comment $PrinterComment -DriverName $PrinterDriverName -PortName $PrinterPortName
} else {
    Write-Host "Printer '$PrinterName' already existing"
    exit
}

$Printer = Get-Printer -Name $PrinterName -erroraction $erroraction
if ($Printer) {
    Write-Host "Added printer '$PrinterName' successfully"
    Get-Printer -Name $PrinterName
    Write-Host ""
} else {
    Write-Error "Failed while adding printer '$PrinterName'"
}

if ($PausePrinter) {
    $wmiPrinter = Get-WmiObject Win32_printer -filter "Name = '$PrinterName'"
    Write-Host "Pause print queue"
    $wmiPrinter.pause()
}
