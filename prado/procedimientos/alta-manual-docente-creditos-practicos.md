---
type: Procedure
title: Alta manual de un docente con créditos prácticos
description: Procedimiento para incorporar manualmente a un docente con créditos prácticos cuando figura sin un grupo concreto y los automatismos de PRADO no pueden asignarlo.
service: PRADO
audience: personal-cau
status: draft
owner: chesco
usual_ticket_category: Gestión manual
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - profesorado
  - creditos-practicos
  - grupo-sg
  - alta-manual
  - gestion-manual
---

# Alta manual de un docente con créditos prácticos

## Objetivo

Determinar si procede incorporar manualmente a un docente con créditos prácticos en un grupo concreto de PRADO y documentar correctamente la actuación.

## Cuándo aplicar este procedimiento

Aplicar cuando:

- el docente figura en la asignación docente oficial;
- tiene asignados créditos prácticos;
- aparece como `SG —Sin Grupo—` o sin un grupo concreto;
- los automatismos no pueden determinar a qué grupo debe incorporarse;
- se solicita su alta en un grupo específico.

## Cuándo no aplicar este procedimiento

No utilizarlo cuando:

- el docente no figura en la asignación docente oficial;
- la asignatura o los créditos no constan en el POD;
- la petición pretende sustituir una asignación docente incorrecta;
- no se ha identificado el grupo de destino;
- se solicita matricular manualmente a un estudiante;
- existe únicamente un retraso de sincronización.

## Datos que hay que solicitar

Obtener los siguientes datos:

- nombre y apellidos del docente;
- correo electrónico institucional;
- plataforma afectada:
  - PRADO Grado;
  - PRADO Posgrado;
- curso académico;
- nombre y código de la asignatura;
- grupo concreto en el que debe incorporarse;
- número o tipo de créditos prácticos asignados;
- persona que solicita el alta;
- relación de esa persona con la asignatura;
- rol que debe asignarse;
- justificación de la petición.

## Comprobaciones previas

### 1. Confirmar la identidad

Comprobar que la cuenta corresponde a la persona docente indicada y que no existe un usuario duplicado o un problema de identificación.

### 2. Consultar la asignación docente oficial

Verificar que la persona:

- figura en el [Plan de Ordenación Docente —POD—](../conceptos-y-reglas/plan-ordenacion-docente.md);
- tiene créditos prácticos asignados;
- aparece como [grupo SG —Sin Grupo—](../conceptos-y-reglas/grupo-sg.md) o sin un grupo concreto.

### 3. Identificar el grupo de destino

Determinar con precisión:

- el grupo al que debe incorporarse;
- el espacio docente correspondiente;
- el rol que necesita.

No realizar el alta si el grupo de destino no está claramente identificado.

### 4. Comprobar quién solicita la actuación

Confirmar que la petición procede de una persona con responsabilidad o participación suficiente en la asignatura, como el profesorado de teoría o la unidad competente.

La solicitud y su justificación deben quedar registradas en el ticket.

### 5. Descartar un retraso de sincronización

Aplicar los [plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md).

El transcurso del plazo no resolverá automáticamente un caso `SG` cuando el sistema no dispone de un grupo concreto, pero debe descartarse que exista una modificación reciente todavía no procesada.

## Árbol de decisión

### Caso 1. Figura oficialmente con créditos prácticos y como SG

Si la información oficial es correcta:

1. identificar el grupo concreto;
2. comprobar que la solicitud está justificada;
3. realizar el alta manual;
4. asignar el rol adecuado;
5. registrar la actuación;
6. clasificar el ticket como [Gestión manual](../iris/gestion-manual.md).

### Caso 2. No figura en la asignación docente oficial

Si la persona no aparece en el POD:

1. no realizar el alta manual ordinaria;
2. informar de que la asignación debe corregirse en origen;
3. remitir a la secretaría del departamento o unidad competente;
4. clasificar el ticket como [Ordenación docente](../iris/ordenacion-docente.md).

### Caso 3. Figura oficialmente, pero no tiene créditos prácticos

Si los datos no coinciden con la petición:

1. no realizar el alta;
2. solicitar que se revise la asignación docente oficial;
3. documentar la discrepancia;
4. clasificar el ticket como `Ordenación docente`.

### Caso 4. No se identifica el grupo de destino

Si la solicitud no indica el grupo:

1. pedir que se especifique el grupo concreto;
2. no realizar una incorporación genérica;
3. mantener el ticket pendiente hasta recibir la información.

### Caso 5. Existe una autorización expresa de Ordenación Académica

Si la actuación está autorizada por escrito:

1. comprobar que la autorización consta en el ticket;
2. verificar asignatura, grupo y rol;
3. realizar únicamente el alta autorizada;
4. registrar la actuación y la autorización;
5. clasificar el ticket como `Gestión manual`.

## Actuación técnica

Cuando proceda el alta:

1. acceder al espacio docente correspondiente;
2. localizar la gestión de participantes;
3. buscar a la persona por su identificador institucional;
4. comprobar que se selecciona la cuenta correcta;
5. asignarla al grupo solicitado;
6. asignar el rol correspondiente;
7. guardar los cambios;
8. verificar que la participación aparece activa;
9. registrar en el ticket:
   - persona incorporada;
   - asignatura;
   - grupo;
   - rol;
   - motivo;
   - persona solicitante;
   - fecha de la actuación.

## Resultado esperado

La persona docente debe:

- aparecer como participante en el espacio correcto;
- estar asociada al grupo solicitado;
- disponer del rol necesario;
- poder acceder a los contenidos correspondientes.

## Clasificación en IRIS

La categoría habitual es:

- [Gestión manual](../iris/gestion-manual.md).

Utilizar `Ordenación docente` cuando la causa real sea una ausencia o un error en la asignación oficial.

## Plantillas de respuesta

### Plantilla 1. Alta realizada

Buenos días, [nombre]:

Se ha realizado el alta de [nombre del docente] en el grupo [grupo] de la asignatura [asignatura], con el rol [rol].

La actuación se ha realizado de forma manual porque el docente figura con créditos prácticos y sin un grupo concreto en la asignación oficial, por lo que PRADO no puede determinar automáticamente el grupo de incorporación.

Un saludo.

---

### Plantilla 2. Falta identificar el grupo

Estimada/o [nombre]:

Para poder tramitar el alta manual necesitamos que nos indique el grupo concreto de la asignatura [asignatura] en el que debe incorporarse [nombre del docente].

La persona figura con créditos prácticos, pero sin un grupo determinado, por lo que PRADO no puede realizar la asignación automática.

Cuando dispongamos de ese dato podremos revisar la solicitud.

Un saludo.

---

### Plantilla 3. La persona no figura en la asignación oficial

Estimada/o [nombre]:

Según la información disponible, [nombre del docente] no figura actualmente en la asignación docente oficial de la asignatura [asignatura].

Desde el CEPRUD no debemos realizar un alta manual ordinaria para sustituir una asignación docente que no consta en origen.

Le recomendamos que solicite a la secretaría del departamento la revisión del Plan de Ordenación Docente. Una vez corregida la información, el cambio se incorporará a PRADO mediante los automatismos establecidos.

Un saludo.

## Conceptos relacionados

- [Grupo SG —Sin Grupo—](../conceptos-y-reglas/grupo-sg.md)
- [Plan de Ordenación Docente —POD—](../conceptos-y-reglas/plan-ordenacion-docente.md)
- [Altas automáticas desde bases de datos oficiales](../conceptos-y-reglas/altas-automaticas.md)
- [Plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md)

## Categorías de IRIS relacionadas

- [Gestión manual](../iris/gestion-manual.md)
- [Ordenación docente](../iris/ordenacion-docente.md)

## Procedimientos relacionados

- [El docente no ve una asignatura o un grupo](docente-no-ve-asignatura.md)
- Alta manual de un docente con autorización de Ordenación Académica
- Docente que figura como SG y necesita asociarse a un grupo
