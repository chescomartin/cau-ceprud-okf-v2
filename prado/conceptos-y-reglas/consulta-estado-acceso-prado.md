---
type: Concept
title: Consulta de Estado para Acceso a PRADO en Oficina Virtual
description: Concepto que explica la utilidad de Oficina Virtual utilizada para comprobar la matrícula y el estado administrativo que condiciona el acceso del alumnado a PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - oficina-virtual
  - acceso
  - matricula
  - incidencia-administrativa
  - alumnado
---

# Consulta de Estado para Acceso a PRADO en Oficina Virtual

## Definición

La **Consulta de Estado para Acceso a PRADO** es una utilidad disponible en la Oficina Virtual de la Universidad de Granada.

Permite consultar información relacionada con:

- la matrícula del alumnado;
- el centro responsable;
- el estado administrativo que puede permitir o impedir el acceso a PRADO;
- la existencia de una incidencia administrativa.

El personal técnico puede utilizar esta información para reproducir o comprobar lo que ve el alumnado en su Oficina Virtual.

## Para qué se utiliza

La consulta resulta especialmente útil cuando un estudiante indica:

- que no puede entrar en PRADO;
- que no ve una asignatura en la que afirma estar matriculado;
- que su expediente estaba bloqueado y ya ha regularizado la situación;
- que ha resuelto un problema de pago;
- que no sabe a qué centro debe dirigirse;
- que aparece vinculado a más de un centro.

## Información disponible

La utilidad permite comprobar, entre otros aspectos:

- las asignaturas en las que figura matriculada la persona;
- el centro o centros relacionados con su situación;
- si existe una incidencia administrativa;
- si la secretaría ya ha actualizado o desbloqueado el expediente.

Cuando aparecen dos centros, el estudiante debe contactar con ambos para aclarar qué unidad debe resolver su situación administrativa.

## Actualización de la información

La base interna indica que la información mostrada en esta consulta se actualiza a partir de los datos grabados por las secretarías.

Para comprobar si una incidencia administrativa ha sido retirada, la información de Oficina Virtual se considera más inmediata que determinados atributos consultables a través del [Proveedor de identidad —IdP—](proveedor-identidad-idp.md).

Debe distinguirse entre:

### Información de Oficina Virtual

- refleja los datos grabados por las secretarías;
- puede mostrar de forma inmediata la retirada de una incidencia administrativa;
- es la referencia principal para esta comprobación en Grado.

### Información recibida por el IdP

- puede tardar más en actualizar determinados atributos;
- la documentación interna utiliza como referencia un plazo de hasta 24 horas;
- técnicamente, el refresco puede producirse una vez por la mañana y otra por la tarde.

## Limitación en Posgrado

La base de conocimiento advierte que esta consulta funciona adecuadamente para Grado, pero no debe utilizarse como única referencia para comprobar la matrícula de Posgrado.

En incidencias de Posgrado, la matrícula debe revisarse mediante las [vistas de bases de datos](vistas-bases-datos.md).

## Comprobaciones del CAU

Ante una incidencia de acceso o matrícula, seguir este orden:

1. confirmar la identidad y el correo institucional;
2. comprobar la plataforma afectada:
   - PRADO Grado;
   - PRADO Posgrado;
3. solicitar o revisar la información de la Consulta de Estado para Acceso a PRADO;
4. comprobar la matrícula mostrada;
5. revisar si existe una incidencia administrativa;
6. identificar el centro o centros responsables;
7. comparar esta información con los atributos del IdP;
8. comprobar la situación actual en PRADO;
9. aplicar los plazos de actualización cuando el desbloqueo sea reciente.

## Árbol de interpretación

### Caso 1. Existe una incidencia administrativa

1. informar de que el acceso está condicionado por la situación administrativa;
2. identificar el centro responsable;
3. indicar al estudiante que contacte con la secretaría correspondiente;
4. clasificar el ticket como `Incidencia administrativa`.

### Caso 2. La incidencia administrativa ya no aparece

1. comprobar cuándo fue retirada;
2. tener en cuenta que PRADO o el IdP pueden conservar temporalmente información anterior;
3. aplicar el plazo de actualización correspondiente;
4. pedir que se pruebe el acceso nuevamente;
5. revisar el caso si el problema continúa después del plazo.

### Caso 3. La matrícula no aparece

1. no realizar una matrícula manual ordinaria;
2. indicar que debe comprobarse en la secretaría;
3. identificar el centro responsable;
4. clasificar el ticket como `Matrícula`.

### Caso 4. La matrícula aparece y no existe incidencia administrativa

1. comprobar la información del IdP;
2. revisar la participación en PRADO;
3. comprobar cachés o actualizaciones pendientes según el procedimiento interno;
4. aplicar el procedimiento específico de acceso.

### Caso 5. La consulta corresponde a Posgrado

1. no basar la conclusión únicamente en Oficina Virtual;
2. comprobar la matrícula en las vistas de bases de datos;
3. comparar el resultado con PRADO;
4. clasificar según la causa comprobada.

## Diferencia entre matrícula, incidencia administrativa y acceso

### Matrícula

La persona no consta oficialmente en la asignatura.

Categoría habitual:

- `Matrícula`.

### Incidencia administrativa

La persona puede tener matrícula, pero su expediente está bloqueado por una causa administrativa, habitualmente relacionada con el pago.

Categoría habitual:

- `Incidencia administrativa`.

### Acceso

La matrícula y la situación administrativa son correctas, pero la persona sigue sin poder autenticarse o entrar en la plataforma.

Categoría habitual:

- `Acceso`.

## Plantilla de respuesta

Estimada/o [nombre]:

Para comprobar su situación, acceda en la Oficina Virtual al apartado **«Consulta de Estado para Acceso a PRADO»**.

En esta consulta podrá revisar:

- las asignaturas en las que figura matriculada/o;
- el centro responsable;
- y si existe alguna incidencia administrativa que esté impidiendo el acceso.

Si aparece una incidencia administrativa, deberá contactar con la secretaría del centro indicado. Si aparecen dos centros, deberá consultar con ambos para aclarar su situación.

Una vez regularizada la incidencia, la actualización en PRADO puede no ser inmediata.

Un saludo.

## Conceptos relacionados

- [Proveedor de identidad —IdP—](proveedor-identidad-idp.md)
- [Vistas de bases de datos](vistas-bases-datos.md)
- [Altas automáticas desde bases de datos oficiales](altas-automaticas.md)
- [Plazos de sincronización y actualización](plazos-sincronizacion.md)
- [Incidencia administrativa](incidencia-administrativa.md)
- [Matrícula manual](../conceptos-y-reglas/matricula-manual.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](../procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso o verificación en dos pasos](../procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [El alumnado está matriculado, pero no puede ver el curso](../procedimientos/alumnado-matriculado-no-ve-curso.md)

## Categorías de IRIS relacionadas

- [Acceso](../iris/acceso.md)
- [Incidencia administrativa](../iris/incidencia-administrativa.md)
- [Matrícula](../iris/matricula.md)
