---
type: Role
title: Rol Editingteacher
description: Definición y limitación documentada del rol Editingteacher en PRADO.
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - usuarios
  - roles
  - editingteacher
  - profesorado
---

# Rol Editingteacher

## Definición

El rol **Editingteacher** es un rol docente utilizado en los espacios de PRADO.

La documentación interna consultada únicamente especifica una limitación concreta de este rol:

- no permite dar de alta a otras personas en el espacio docente con rol de docente.

## Diferencia principal con Manageteacher

No debe confundirse con el rol:

- [Manageteacher](/prado/usuarios-y-roles/rol-manageteacher.md)

La diferencia documentada es:

- `Editingteacher`: no puede incorporar usuarios con rol docente;
- `Manageteacher`: sí puede incorporar usuarios con rol docente.

## Consecuencia para la gestión

Cuando una persona con rol `Editingteacher` solicita incorporar a otro docente, debe comprobarse:

1. el rol real que tiene en el espacio;
2. la asignación docente oficial de la persona que se quiere incorporar;
3. si existe una persona con rol `Manageteacher`;
4. si procede una actuación técnica;
5. si es necesaria una autorización de Ordenación Académica.

## Casos frecuentes

### No puede añadir a otro docente

Debe comprobarse que su rol es `Editingteacher`.

Esta limitación es propia del rol y no implica necesariamente un error de funcionamiento de PRADO.

### Solicita que se le cambie el rol

No debe modificarse el rol únicamente para permitirle añadir a otra persona.

Antes debe comprobarse:

- el tipo de espacio;
- la función que desempeña;
- la asignación docente;
- quién autoriza el cambio;
- y si el rol solicitado corresponde realmente.

### Afirma que coordina la asignatura

La condición declarada de coordinador o coordinadora de asignatura no implica automáticamente que deba tener el rol `Manageteacher`.

Consultar:

- [Coordinador o coordinadora de asignatura](/prado/usuarios-y-roles/coordinador-asignatura.md)

## Información que debe registrarse

Anotar:

- nombre y correo institucional;
- plataforma;
- curso académico;
- espacio docente;
- rol actual;
- actuación solicitada;
- persona que se desea incorporar;
- asignación docente consultada;
- autorización disponible;
- respuesta facilitada.

## Procedimientos relacionados

- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)
- [Alta manual con autorización de Ordenación Académica](/prado/procedimientos/alta-manual-autorizacion-ordenacion-academica.md)
- [Docente no ve una asignatura](/prado/procedimientos/docente-no-ve-asignatura.md)

## Categorías de IRIS relacionadas

- [Gestión manual](/prado/iris/gestion-manual.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)

## Alcance de esta ficha

La documentación fuente no detalla el conjunto completo de permisos del rol `Editingteacher`.

Esta ficha recoge únicamente la diferencia expresamente documentada respecto a la incorporación de usuarios con rol docente.
