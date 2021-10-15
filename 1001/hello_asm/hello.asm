SECTION .data
hello: db 'Hello, World',0x0a

SECTION .text
global _start
_start:
	xor rdi, rdi
	lea rsi, [hello]
	mov rdx, 14
	mov rax, 1
	syscall
	xor rdi, rdi
	mov rax, 60
	syscall


