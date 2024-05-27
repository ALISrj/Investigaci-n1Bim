import asyncio

async def tarea1():
    print('Tarea 1 iniciada')
    await asyncio.sleep(2)
    print('Tarea 1 completada')

async def tarea2():
    print('Tarea 2 iniciada')
    await asyncio.sleep(4)
    print('Tarea 2 completada')

async def main():
    # Crea las tareas
    tarea_1 = asyncio.create_task(tarea1())
    tarea_2 = asyncio.create_task(tarea2())

    # Ejecuta las tareas
    await tarea_1
    await tarea_2

# Ejecuta la función principal
asyncio.run(main())
