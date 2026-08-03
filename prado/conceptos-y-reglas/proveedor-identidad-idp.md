---
type: Concept
title: Proveedor de identidad —IdP—
abbreviation: IdP
description: Concepto que explica el sistema institucional de autenticación utilizado para acceder a PRADO con la cuenta de correo de la Universidad de Granada.
service: PRADO
audience: personal-cau
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - idp
  - autenticacion
  - acceso
  - cuenta-institucional
  - csirc
---

# Proveedor de identidad —IdP—

## Definición

`IdP` significa **Proveedor de Identidad**.

Es el sistema institucional que proporciona a PRADO la información necesaria para autenticar a las personas usuarias mediante su cuenta de correo de la Universidad de Granada.

PRADO utiliza esta autenticación institucional para permitir el acceso con las credenciales correspondientes.

## Relación con PRADO

La información de autenticación es suministrada desde el CSIRC para que PRADO, junto con otros servicios de la Universidad de Granada, pueda reconocer a la persona usuaria.

El IdP permite:

- identificar a la persona que intenta acceder;
- comprobar determinados atributos institucionales;
- vincular la autenticación con la cuenta de correo correspondiente;
- proporcionar información asociada al curso académico vigente.

## Información consultable

El personal técnico puede disponer de herramientas internas para consultar la información de identidad asociada a una cuenta de correo.

Estas consultas pueden ayudar a comprobar:

- si la cuenta institucional aparece correctamente;
- los atributos recibidos para el curso académico vigente;
- si existe una discrepancia entre la identidad y la participación en PRADO;
- si el problema está en la autenticación o en los datos académicos.

No deben incluirse en respuestas públicas direcciones técnicas internas ni datos que no sean necesarios para resolver la consulta.

## Cambio de curso académico

La información de atributos del IdP corresponde al curso académico en vigor.

La base interna indica que el cambio de curso académico se efectúa el primer día laborable de septiembre.

Este dato debe revisarse periódicamente antes de considerarlo una regla permanente.

## Diferencia entre autenticación y participación

Debe distinguirse entre:

### Problema de autenticación

La persona no puede identificarse o entrar en PRADO con su cuenta institucional.

La causa puede estar relacionada con:

- las credenciales;
- la cuenta institucional;
- los atributos suministrados por el IdP;
- una incidencia administrativa;
- otro problema de acceso.

### Problema de participación

La persona puede entrar en PRADO, pero no aparece en una asignatura o grupo.

En este caso, la causa suele estar relacionada con:

- la matrícula oficial;
- el [Plan de Ordenación Docente —POD—](plan-ordenacion-docente.md);
- las [altas automáticas desde bases de datos oficiales](altas-automaticas.md);
- los [plazos de sincronización y actualización](plazos-sincronizacion.md);
- una actuación manual excepcional.

## Comprobaciones del CAU

Ante una incidencia de acceso, comprobar:

1. la dirección de correo utilizada;
2. la plataforma afectada:
   - PRADO Grado;
   - PRADO Posgrado;
3. el curso académico;
4. el mensaje de error;
5. si la cuenta institucional funciona en otros servicios;
6. la información disponible en las herramientas internas de consulta;
7. el estado de acceso en la Oficina Virtual;
8. si el problema es de autenticación o de participación.

## Clasificación orientativa en IRIS

La categoría habitual es:

- `Acceso`: la persona no puede autenticarse o entrar en la plataforma.

Utilizar otra categoría cuando la causa comprobada sea diferente:

- `Incidencia administrativa`: existe un bloqueo administrativo que impide el acceso.
- [Ordenación docente](../iris/ordenacion-docente.md): el docente entra en PRADO, pero no aparece en su asignatura.
- `Matrícula`: el estudiante entra en PRADO, pero no consta correctamente en una asignatura.
- `Usuario/rol duplicado`: existe una duplicidad de identidad o participación.

## Conceptos relacionados

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](consulta-estado-acceso-prado.md)
- [Vistas de bases de datos](vistas-bases-datos.md)
- [Altas automáticas desde bases de datos oficiales](altas-automaticas.md)
- [Plazos de sincronización y actualización](plazos-sincronizacion.md)

## Procedimientos relacionados

- [Problemas de acceso o verificación en dos pasos](../procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- Comprobación del estado de acceso
- [El docente no ve una asignatura o un grupo](../procedimientos/docente-no-ve-asignatura.md)
- [Acceso de un docente externo](../procedimientos/acceso-docente-externo.md)
