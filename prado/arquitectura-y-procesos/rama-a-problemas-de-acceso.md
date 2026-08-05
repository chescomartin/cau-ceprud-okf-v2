---
type: DecisionTree
title: Rama A — Problemas de acceso a PRADO
description: Rama del árbol general para las personas que no consiguen entrar en la plataforma.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-11-05
last_reviewed: 2026-08-05
tags:
  - prado
  - arbol-decision
  - clasificacion
  - acceso
---

# Rama A — Problemas de acceso a PRADO

> **Se llega a esta rama** desde el
> [árbol general de decisión](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md), pregunta 1, cuando la
> persona **no consigue entrar en la plataforma**. Si entra pero no ve algo, la rama no
> es esta.

## A1. ¿Es un problema de autenticación?

Comprobar:

- cuenta utilizada;
- dominio del correo;
- proveedor de identidad;
- contraseña;
- verificación en dos pasos;
- tipo de usuario.

Procedimientos aplicables:

- [Problemas de acceso o verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [Acceso de un docente externo](/prado/procedimientos/acceso-docente-externo.md)

## A2. ¿Existe incidencia administrativa?

### Sí

Comprobar Oficina Virtual, el atributo del IdP, la caché de acceso y el centro o centros
que aparecen.

- Regla: [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- Categoría: [IRIS: Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

### No

Continuar comprobando el IdP, el perfil de usuario, la existencia de cuenta duplicada y
que la plataforma sea la correcta.

## A3. ¿La persona es un usuario manual?

### Sí

Comprobar el método de identificación `Cuentas manuales`, que dispone de credenciales
propias y que no puede acceder mediante SAML.

- Concepto: [Usuario manual](/prado/usuarios-y-roles/usuario-manual.md)

### No

Continuar con la cuenta institucional.

## Desenlaces de esta rama

| Situación comprobada | Categoría de IRIS |
|---|---|
| Bloqueo administrativo del expediente | [Incidencia administrativa](/prado/iris/incidencia-administrativa.md) |
| Fallo de autenticación con la situación administrativa correcta | [Acceso](/prado/iris/acceso.md) |
| Duplicidad de identidad o de participación | [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md) |
| Causa no determinada tras las comprobaciones | [Sin resolver](/prado/iris/sin-resolver.md) |

## Volver

- [Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
