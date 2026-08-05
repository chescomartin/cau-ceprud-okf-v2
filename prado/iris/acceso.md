---
type: TicketCategory
title: "IRIS: Acceso"
description: Tema de ayuda para tickets en los que una persona no puede autenticarse o entrar en PRADO.
regla_aplicable: /prado/conceptos-y-reglas/consulta-estado-acceso-prado.md
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - iris
  - acceso
  - autenticacion
  - idp
  - cuenta-institucional
---

# IRIS: Acceso

> **Alcance de esta ficha: únicamente la clasificación del ticket.**
>
> Qué es el fenómeno y por qué se produce: [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md).
> Qué se le escribe a la persona usuaria: [respuestas tipo](/respuestas-tipo/index.md).


## Definición

Utilizar esta categoría cuando una persona no puede autenticarse o entrar en PRADO y la causa principal no es una incidencia administrativa, un problema de matrícula ni una ausencia de asignación docente.

La categoría se refiere al acceso a la plataforma, no a la visibilidad de una asignatura concreta después de haber entrado.

## Cuándo utilizar esta categoría

Utilizar `Acceso` cuando:

- la persona no puede entrar en PRADO;
- las credenciales o la cuenta institucional no permiten completar la autenticación;
- existe un problema relacionado con el [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md);
- se consulta un olvido de contraseña;
- un docente externo no consigue acceder con la cuenta institucional habilitada;
- la matrícula o asignación son correctas, pero el acceso a la plataforma continúa fallando;
- la situación administrativa es correcta y no existe un bloqueo del expediente.

## Cuándo no utilizar esta categoría

No utilizar `Acceso` cuando:

- existe una [incidencia administrativa](/prado/iris/incidencia-administrativa.md);
- el estudiante no consta oficialmente matriculado;
- el docente entra en PRADO, pero no ve una asignatura o grupo;
- el espacio existe, pero está oculto;
- la participación está suspendida o no activa;
- existe un usuario o rol duplicado;
- todavía no se ha identificado la causa después de las comprobaciones.

## Comprobaciones previas

Antes de clasificar el ticket:

1. confirmar el nombre, correo institucional y tipo de usuario;
2. comprobar la plataforma afectada:
   - PRADO Grado;
   - PRADO Posgrado;
3. solicitar el mensaje de error exacto;
4. comprobar si la cuenta funciona en otros servicios institucionales;
5. revisar la información disponible en el IdP;
6. consultar el estado administrativo mediante la [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md);
7. comprobar la matrícula o asignación oficial cuando corresponda;
8. distinguir entre un problema para entrar en la plataforma y un problema para ver un curso.

## Pregunta de control

Antes de elegir esta categoría, comprobar:

> ¿La persona no puede autenticarse o entrar en PRADO aunque su situación académica y administrativa sea correcta?

- Si la respuesta es sí, utilizar `Acceso`.
- Si existe un bloqueo del expediente, utilizar `Incidencia administrativa`.
- Si falta la matrícula oficial, utilizar `Matrícula`.
- Si el docente entra, pero no ve su asignatura, utilizar `Ordenación docente`.
- Si la causa sigue sin determinarse, utilizar `Sin resolver`.

## Árbol de clasificación

### No puede entrar y existe incidencia administrativa

Categoría:

- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md).

### No puede entrar y no consta la matrícula

Categoría:

- `Matrícula`.

### No puede entrar y la situación oficial es correcta

Categoría:

- `Acceso`.

### Puede entrar, pero no ve una asignatura o grupo

Categoría:

- [Ordenación docente](/prado/iris/ordenacion-docente.md), si afecta al profesorado.
- `Matrícula`, si afecta al alumnado.

### Puede entrar, pero el curso está oculto

Categoría:

- `Visibilidad`.

### Existe duplicidad de cuenta o rol

Categoría:

- `Usuario/rol duplicado`.

## Casos de ejemplo

### Ejemplo 1. Olvido de contraseña

La persona no puede completar la autenticación porque no recuerda sus credenciales.

Categoría:

- `Acceso`.

### Ejemplo 2. Docente externo sin acceso

El docente externo dispone de una cuenta institucional habilitada, pero no puede entrar en PRADO.

Categoría:

- `Acceso`.

Debe comprobarse primero que la cuenta está correctamente creada y que corresponde a la plataforma afectada.

### Ejemplo 3. Expediente bloqueado

El estudiante no puede entrar y en Oficina Virtual aparece una incidencia administrativa.

Categoría:

- `Incidencia administrativa`.

### Ejemplo 4. Entra en PRADO, pero falta una asignatura

La autenticación se completa correctamente.

Categoría:

- no utilizar `Acceso`;
- clasificar según matrícula, ordenación docente o visibilidad.

## Plantilla de respuesta

Estimada/o [nombre]:

Para revisar el problema de acceso a PRADO necesitamos que nos facilite:

- la dirección de correo institucional con la que intenta acceder;
- la plataforma afectada: PRADO Grado o PRADO Posgrado;
- el mensaje de error exacto;
- y una captura de pantalla, cuando sea posible.

También debe comprobar en su Oficina Virtual el apartado **«Consulta de Estado para Acceso a PRADO»**, para descartar que exista una incidencia administrativa.

Cuando dispongamos de esta información podremos determinar si el problema corresponde a la autenticación o a otra causa.

Un saludo.

## Conceptos relacionados

- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Docente externo](/prado/usuarios-y-roles/docente-externo.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso o verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [Acceso de un docente externo](/prado/procedimientos/acceso-docente-externo.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)

## Categorías relacionadas

- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Visibilidad](/prado/iris/visibilidad.md)
- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)
- [Sin resolver](/prado/iris/sin-resolver.md)
