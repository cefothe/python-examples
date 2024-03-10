chiclo = int(input())

stotichi = int(chiclo /100)
edinichi = int(chiclo %10)

if stotichi == edinichi:
    print("Palindrom")
else:
    print("Obiknoveno cislo")