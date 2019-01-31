global _start

section .data
    memory TIMES 256 db 0
    memp db 0

section .text

; >
mempp :
    inc byte [memp]
    ret

; >
mempm :
    dec byte [memp]
    ret

; +
memoryp :
    mov edx, [memp]
    inc byte [memory+edx]
    ret

; -
memorym :
    mov edx, [memp]
    dec byte [memory+edx]
    ret

; .
print :
    mov eax, 4
    mov ebx, 1
    mov ecx, [memp]
    add ecx, memory
    mov edx, 1
    int 0x80
    ret

; ,
input :
    mov eax, 3
    mov ebx, 0
    mov ecx, [memp]
    add ecx, memory
    mov edx, 1
    int 0x80
    ret

end_prg :
    mov eax, 1
    mov ebx, 0
    int 0x80

_start :
