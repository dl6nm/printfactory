$PrinterName = "BlackHole"
$PrinterPortName = "BlackHole"
$PrinterDriverName = "Generic / Text Only"

$erroraction = 'silentlycontinue'

$Printer = Get-Printer -Name $PrinterName -erroraction $erroraction
if ($Printer) {
    Write-Host "Removing printer '$PrinterName'"
    Remove-Printer -Name $PrinterName
}

$PrinterDriver = Get-PrinterDriver -Name $PrinterDriverName -erroraction $erroraction
if ($PrinterDriver) {
    Write-Host "Removing printer driver '$PrinterDriverName'"
    Remove-PrinterDriver -Name $PrinterDriverName
}

$PrinterPort = Get-PrinterPort -Name $PrinterPortName -erroraction $erroraction
if ($PrinterPort) {
    Write-Host "Removing printer port '$PrinterPortName'"
    Remove-PrinterPort -Name $PrinterPortName
}
