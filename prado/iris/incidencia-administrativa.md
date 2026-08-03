---
type: TicketCategory
title: Incidencia administrativa
description: Tema de ayuda para tickets en los que un bloqueo administrativo del expediente impide al alumnado acceder a PRADO.
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
status: draft
language: es
last_reviewed: 2026-08-03
tags:
  - iris
  - incidencia-administrativa
  - acceso
  - alumnado
  - matricula
  - oficina-virtual
---

# Incidencia administrativa

## Definición

Utilizar esta categoría cuando el acceso del alumnado a PRADO está impedido por una incidencia administrativa registrada en su expediente.

La causa suele estar relacionada con la situación administrativa de la matrícula, por ejemplo un problema de pago, aunque debe comprobarse el caso concreto antes de clasificar el ticket.

## Cuándo utilizar esta categoría

Utilizar `Incidencia administrativa` cuando:

- la Consulta de Estado para Acceso a PRADO muestra una incidencia administrativa;
- el expediente del estudiante está bloqueado desde la secretaría;
- el acceso está impedido por una situación administrativa pendiente;
- la secretaría ya ha retirado el bloqueo, pero el cambio todavía no se ha actualizado en el IdP o en PRADO;
- el estudiante necesita identificar el centro responsable de regularizar su expediente.

## Cuándo no utilizar esta categoría

No utilizar `Incidencia administrativa` cuando:

- no existe ningún bloqueo administrativo;
- el estudiante no consta oficialmente matriculado;
- la matrícula es correcta, pero el usuario no puede autenticarse;
- la persona entra en PRADO, pero no ve una asignatura;
- el problema afecta a la asignación docente del profesorado;
- no se ha podido determinar la causa después de las comprobaciones.

## Comprobaciones previas

Antes de clasificar el ticket:

1. confirmar la identidad y el correo institucional;
2. comprobar la plataforma afectada;
3. revisar la [Consulta de Estado para Acceso a PRADO en Oficina Virtual](../conceptos-y-reglas/consulta-estado-acceso-prado.md);
4. comprobar si aparece una incidencia administrativa;
5. identificar el centro o centros responsables;
6. confirmar si la secretaría ya ha desbloqueado el expediente;
7. revisar la información recibida mediante el [Proveedor de identidad —IdP—](../conceptos-y-reglas/proveedor-identidad-idp.md);
8. tener en cuenta los plazos de actualización y la caché de PRADO.

## Pregunta de control

Antes de elegir esta categoría, comprobar:

> ¿Existe un bloqueo administrativo del expediente que explica el problema de acceso?

- Si la respuesta es sí, utilizar `Incidencia administrativa`.
- Si falta la matrícula oficial, utilizar `Matrícula`.
- Si la situación administrativa es correcta y el problema es de autenticación, utilizar `Acceso`.
- Si la causa sigue sin determinarse, utilizar `Sin resolver`.

## Árbol de clasificación

### La incidencia continúa activa

Categoría:

- `Incidencia administrativa`.

Actuación:

- remitir al estudiante a la secretaría del centro responsable;
- explicar que el CEPRUD no puede retirar el bloqueo.

### La incidencia ya se ha retirado recientemente

Categoría:

- `Incidencia administrativa`.

Actuación:

- aplicar el plazo de actualización;
- comprobar posteriormente el IdP y PRADO;
- escalar si el bloqueo continúa después del plazo.

### No existe incidencia, pero falta la matrícula

Categoría:

- `Matrícula`.

### No existe incidencia y la matrícula es correcta

Categoría:

- `Acceso`, cuando el problema sea de autenticación o entrada en la plataforma.

### No se identifica la causa

Categoría:

- `Sin resolver`.

## Casos de ejemplo

### Ejemplo 1. Bloqueo por situación de pago

El estudiante no puede acceder y en Oficina Virtual aparece una incidencia administrativa.

Categoría:

- `Incidencia administrativa`.

### Ejemplo 2. Expediente desbloqueado esta mañana

La incidencia ya no aparece en Oficina Virtual, pero PRADO todavía impide el acceso.

Categoría:

- `Incidencia administrativa`.

Debe esperarse la actualización de los atributos y de la caché antes de reclasificar.

### Ejemplo 3. No aparece matriculado

No existe incidencia administrativa, pero la asignatura no figura en la matrícula oficial.

Categoría:

- `Matrícula`.

### Ejemplo 4. Todo es correcto, pero no puede autenticarse

La matrícula y la situación administrativa son correctas.

Categoría:

- `Acceso`.

## Plantilla de respuesta

Estimada/o [nombre]:

Hemos comprobado que existe una incidencia administrativa asociada a su expediente que está impidiendo el acceso a PRADO.

Debe contactar con la secretaría del centro que aparece en el apartado **«Consulta de Estado para Acceso a PRADO»** de su Oficina Virtual.

Desde el CEPRUD no podemos modificar ni retirar este bloqueo administrativo. Una vez regularizada la situación, la actualización del acceso puede no ser inmediata.

Un saludo.

## Regla relacionada

- [Incidencia administrativa](../conceptos-y-reglas/incidencia-administrativa.md)

## Conceptos relacionados

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](../conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Proveedor de identidad —IdP—](../conceptos-y-reglas/proveedor-identidad-idp.md)
- [Vistas de bases de datos](../conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md)
- [Transferencia de tickets en IRIS](../conceptos-y-reglas/transferencia-tickets-iris.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](../procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso o verificación en dos pasos](../procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [El alumnado está matriculado, pero no puede ver el curso](../procedimientos/alumnado-matriculado-no-ve-curso.md)

## Categorías relacionadas

- [Acceso](acceso.md)
- [Matrícula](matricula.md)
- Sin resolver
