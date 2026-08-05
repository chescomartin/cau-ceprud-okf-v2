---
type: Procedure
title: Alta manual de un docente con autorización de Ordenación Académica
description: Procedimiento para realizar una incorporación manual en PRADO cuando existe una autorización expresa y escrita de Ordenación Académica.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
usual_ticket_category: Gestión manual
language: es
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - profesorado
  - alta-manual
  - ordenacion-academica
  - autorizacion
  - gestion-manual
---

# Alta manual de un docente con autorización de Ordenación Académica

## Objetivo

Comprobar y ejecutar una incorporación manual de profesorado en PRADO cuando Ordenación Académica haya autorizado expresamente la actuación.

## Cuándo aplicar este procedimiento

Aplicar cuando:

- la incorporación no puede realizarse mediante los automatismos ordinarios;
- Ordenación Académica ha autorizado expresamente el alta manual;
- la autorización consta por escrito en el ticket;
- se han identificado con precisión la persona, la asignatura, el grupo y el rol.

## Cuándo no aplicar este procedimiento

No utilizarlo cuando:

- no existe una autorización escrita;
- la autorización se ha comunicado únicamente de forma verbal;
- faltan la asignatura, el grupo o el rol de destino;
- la petición pretende corregir una asignación oficial inexistente sin intervención de la unidad competente;
- todavía no ha transcurrido el plazo normal de sincronización;
- la actuación solicitada excede lo autorizado.

## Datos que hay que solicitar

Obtener o comprobar:

- nombre y apellidos del docente;
- correo electrónico institucional;
- plataforma afectada:
  - PRADO Grado;
  - PRADO Posgrado;
- curso académico;
- nombre y código de la asignatura;
- grupo de destino;
- rol que debe asignarse;
- motivo de la solicitud;
- autorización escrita de Ordenación Académica;
- persona o unidad que emite la autorización;
- fecha de la autorización;
- alcance exacto de la actuación autorizada.

## Comprobaciones previas

### 1. Verificar la autorización

Comprobar que la autorización:

- está incorporada al ticket;
- procede de Ordenación Académica;
- identifica el caso concreto;
- especifica o permite determinar la actuación;
- no está condicionada a información adicional.

No debe realizarse el alta si la autorización no puede verificarse.

### 2. Comprobar la identidad del docente

Verificar:

- la cuenta institucional;
- que no existe un usuario duplicado;
- que se selecciona a la persona correcta;
- que la cuenta puede utilizarse en la plataforma correspondiente.

### 3. Comprobar la asignatura y el grupo

Confirmar:

- el curso académico;
- la asignatura exacta;
- el código de la asignatura;
- el grupo o espacio docente de destino;
- que el espacio existe y es el adecuado.

### 4. Determinar el rol

Comprobar el rol autorizado o necesario para la actuación.

No asignar permisos superiores a los solicitados o autorizados.

### 5. Revisar la información oficial

Consultar, cuando sea necesario:

- el [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md);
- los datos disponibles en las vistas de bases de datos;
- la situación actual de la persona en PRADO;
- los [plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md).

La autorización permite realizar la actuación manual, pero no debe ocultar una posible incidencia que también deba corregirse en origen.

## Árbol de decisión

### Caso 1. La autorización es válida y contiene todos los datos

1. comprobar la identidad;
2. localizar el espacio correcto;
3. realizar el alta manual;
4. asignar el grupo y el rol autorizados;
5. verificar el resultado;
6. registrar la actuación en el ticket;
7. clasificar como [Gestión manual](/prado/iris/gestion-manual.md).

### Caso 2. Existe autorización, pero faltan datos

1. no realizar todavía el alta;
2. solicitar la asignatura, el grupo, el rol o cualquier otro dato necesario;
3. mantener el ticket pendiente;
4. continuar cuando la información esté completa.

### Caso 3. La autorización no consta por escrito

1. no realizar la actuación;
2. solicitar que la autorización se incorpore al ticket;
3. explicar que debe quedar registrada;
4. mantener el ticket pendiente.

### Caso 4. La petición supera lo autorizado

1. realizar únicamente la actuación expresamente autorizada;
2. solicitar una nueva autorización para cualquier modificación adicional;
3. dejar constancia de la limitación en el ticket.

### Caso 5. El alta ya se ha producido automáticamente

1. comprobar que la persona aparece correctamente;
2. verificar grupo y rol;
3. no duplicar la participación;
4. informar de que la situación ya está regularizada;
5. cerrar o reclasificar el ticket según corresponda.

## Actuación técnica

Cuando proceda:

1. acceder al espacio docente autorizado;
2. abrir la gestión de participantes;
3. buscar al docente mediante su identificador institucional;
4. comprobar que se selecciona la cuenta correcta;
5. realizar el alta;
6. asociar el grupo indicado;
7. asignar el rol autorizado;
8. guardar los cambios;
9. verificar que la participación está activa;
10. comprobar que no se ha generado una participación duplicada.

## Información que debe registrarse en el ticket

Anotar:

- nombre de la persona incorporada;
- asignatura y código;
- grupo;
- rol;
- fecha de la actuación;
- motivo del alta manual;
- unidad o persona que autorizó;
- referencia o texto de la autorización;
- resultado de la comprobación final;
- nombre del técnico que realizó la actuación.

## Resultado esperado

El docente debe:

- aparecer en el espacio correcto;
- estar asociado al grupo autorizado;
- disponer únicamente del rol necesario;
- poder acceder a la asignatura;
- no tener participaciones duplicadas.

## Clasificación en IRIS

La categoría habitual es:

- [Gestión manual](/prado/iris/gestion-manual.md).

No utilizar `Ordenación docente` como categoría principal cuando la resolución efectiva del ticket haya consistido en una actuación manual autorizada.

## Plantillas de respuesta

### Plantilla 1. Alta realizada

Buenos días, [nombre]:

De acuerdo con la autorización de Ordenación Académica incorporada al ticket, se ha realizado el alta manual de [nombre del docente] en el grupo [grupo] de la asignatura [asignatura], con el rol [rol].

La participación se encuentra activa en PRADO.

Un saludo.

---

### Plantilla 2. Falta la autorización escrita

Estimada/o [nombre]:

Para poder realizar el alta manual solicitada, necesitamos que la autorización de Ordenación Académica quede incorporada por escrito en este ticket.

La autorización debe permitir identificar la persona, la asignatura, el grupo y la actuación que debe realizarse.

Una vez recibida, podremos continuar con la comprobación del caso.

Un saludo.

---

### Plantilla 3. Faltan datos para realizar el alta

Estimada/o [nombre]:

Hemos recibido la autorización para revisar el alta manual, pero necesitamos completar los siguientes datos:

- [dato pendiente];
- [dato pendiente];
- [dato pendiente].

Cuando dispongamos de esta información podremos realizar la actuación autorizada.

Un saludo.

---

### Plantilla 4. El alta ya se ha producido automáticamente

Buenos días, [nombre]:

Hemos comprobado que [nombre del docente] ya figura en el grupo [grupo] de la asignatura [asignatura], con el rol [rol].

Por tanto, no ha sido necesario realizar una nueva incorporación manual.

Un saludo.

## Conceptos relacionados

- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)

## Categorías de IRIS relacionadas

- [Gestión manual](/prado/iris/gestion-manual.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)

## Procedimientos relacionados

- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)
- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [Transferencia de tickets en IRIS](/prado/conceptos-y-reglas/transferencia-tickets-iris.md)
