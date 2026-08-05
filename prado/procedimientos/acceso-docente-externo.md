---
type: Procedure
title: Acceso de un docente externo
description: Procedimiento para atender incidencias de acceso a PRADO de personas que imparten docencia sin formar parte del personal de la UGR.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
usual_ticket_category: Acceso
language: es
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - acceso
  - docente-externo
  - posgrado
  - titulos-propios
  - oficina-virtual
---

# Acceso de un docente externo

## Definición

Un docente externo es una persona que no forma parte del personal de la Universidad de Granada, pero imparte docencia en una actividad académica gestionada mediante PRADO.

Según la base interna, esta figura se utiliza en:

- PRADO Posgrado;
- Títulos Propios.

## Objetivo

Comprobar si el docente externo dispone de la cuenta necesaria para acceder y determinar si la incidencia corresponde a:

- creación o habilitación pendiente de la cuenta;
- desconocimiento del PIN necesario para realizar el trámite;
- uso de una cuenta incorrecta;
- problema de autenticación;
- verificación en dos pasos;
- o falta de participación en el espacio docente después de haber accedido.

## Cuándo aplicar este procedimiento

Aplicar cuando una persona indique, por ejemplo:

- que imparte docencia, pero no pertenece al personal de la UGR;
- que no puede entrar en PRADO Posgrado;
- que no sabe qué cuenta debe utilizar;
- que no puede completar el trámite de creación de la cuenta;
- que no dispone del PIN solicitado en Oficina Virtual;
- que dispone de una cuenta externa, pero la autenticación falla;
- que puede entrar en PRADO, pero no ve el espacio en el que debe impartir docencia.

## Datos que hay que solicitar

Obtener los siguientes datos:

- nombre y apellidos;
- correo electrónico de contacto;
- titulación, máster o actividad académica;
- asignatura o espacio docente;
- curso académico;
- indicación de si pertenece o no al personal de la UGR;
- cuenta institucional que intenta utilizar;
- confirmación de si ya realizó el trámite en Oficina Virtual;
- mensaje de error exacto;
- captura de pantalla, cuando sea posible.

## Comprobaciones iniciales

### 1. Confirmar que se trata de un docente externo

Comprobar que:

- no pertenece al personal de la UGR;
- imparte docencia en Posgrado o en un Título Propio;
- la consulta no corresponde a un docente oficial de Grado.

### 2. Confirmar la cuenta de acceso

Los docentes externos acceden mediante una cuenta creada a través de Oficina Virtual.

La base interna identifica estas cuentas con un formato similar a:

```text
ext...@ugr.es
```

Debe comprobarse:

- que la cuenta ya ha sido creada;
- que se utiliza esa cuenta y no una dirección personal;
- que la dirección está correctamente escrita;
- que la persona conoce las credenciales correspondientes.

### 3. Comprobar el PIN de Oficina Virtual

Para realizar el trámite de creación de la cuenta externa en Oficina Virtual se necesita un PIN.

Según la base interna, este PIN lo proporciona la Escuela Internacional de Posgrado —EIP—.

Cuando la persona no dispone del PIN, debe contactar con la EIP o con la unidad académica responsable para obtenerlo.

### 4. Distinguir acceso y participación

Debe diferenciarse entre:

#### Problema de acceso

La persona no puede autenticarse ni entrar en PRADO.

Categoría habitual:

- [Acceso](/prado/iris/acceso.md).

#### Problema de participación

La persona entra en PRADO, pero no aparece en la asignatura o espacio docente.

En este caso debe comprobarse:

- que la cuenta utilizada coincide con la asociada a la docencia;
- que la incorporación al espacio se ha tramitado;
- que la participación no está suspendida o inactiva;
- qué unidad o responsable debe confirmar la incorporación.

## Árbol de decisión

### Caso 1. No se ha creado la cuenta externa

1. informar de que necesita una cuenta externa creada mediante Oficina Virtual;
2. indicar que el PIN necesario lo proporciona la EIP;
3. no tratar el caso como un fallo técnico de PRADO mientras la cuenta no exista;
4. mantener el ticket pendiente de que se complete el trámite o derivarlo según el circuito interno.

### Caso 2. No dispone del PIN

1. indicar que debe solicitarlo a la EIP o a la unidad académica responsable;
2. explicar que el PIN es necesario para completar el trámite en Oficina Virtual;
3. no solicitar que comunique el PIN dentro del ticket.

### Caso 3. La cuenta existe, pero no puede entrar

1. confirmar que utiliza la cuenta externa correcta;
2. solicitar el mensaje de error;
3. comprobar la información disponible en el [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md);
4. aplicar [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md);
5. revisar la [verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md) cuando el error corresponda al 2FA;
6. clasificar como [Acceso](/prado/iris/acceso.md).

### Caso 4. Puede entrar, pero no ve la asignatura

1. confirmar la cuenta con la que ha accedido;
2. comprobar la asignatura, el curso académico y el espacio docente;
3. revisar si la cuenta está incorporada al espacio;
4. distinguir entre falta de alta, participación suspendida o participación no activa;
5. clasificar según la causa comprobada, no como `Acceso`.

### Caso 5. Intenta entrar en PRADO Grado como docente externo

La base interna limita la figura de docente externo a Posgrado y Títulos Propios.

Antes de realizar otra actuación:

1. comprobar la naturaleza de la docencia;
2. confirmar con la unidad responsable qué tipo de vinculación debe utilizarse;
3. no asumir que el procedimiento de cuenta externa de Posgrado es aplicable a Grado.

## Resultado esperado

Al finalizar la comprobación debe quedar identificado:

- si la persona es realmente un docente externo;
- si dispone de la cuenta externa;
- si ha completado el trámite de Oficina Virtual;
- si necesita solicitar el PIN a la EIP;
- si el problema es de autenticación;
- si el problema es de verificación en dos pasos;
- o si puede entrar, pero falta su participación en el espacio docente.

## Plantillas de respuesta

### Plantilla 1. Debe crear la cuenta externa

Estimada/o [nombre]:

Para acceder como docente externo a PRADO Posgrado necesita disponer de una cuenta externa de la UGR, que debe tramitarse mediante Oficina Virtual.

Para completar el trámite necesitará el PIN facilitado por la Escuela Internacional de Posgrado.

Cuando disponga de la cuenta, deberá utilizarla para acceder a la plataforma.

Un saludo.

---

### Plantilla 2. No dispone del PIN

Estimada/o [nombre]:

El PIN necesario para completar en Oficina Virtual la creación de la cuenta de docente externo debe ser facilitado por la Escuela Internacional de Posgrado o por la unidad académica responsable.

Por motivos de seguridad, no debe enviar el PIN dentro de este ticket.

Un saludo.

---

### Plantilla 3. La cuenta existe, pero no puede entrar

Estimada/o [nombre]:

Para revisar el problema necesitamos que nos facilite:

- la cuenta externa con la que intenta acceder;
- el mensaje de error exacto;
- la plataforma afectada;
- y una captura de pantalla, cuando sea posible.

Comprobaremos si el problema corresponde a la autenticación o a la verificación en dos pasos.

Un saludo.

---

### Plantilla 4. Puede entrar, pero no ve el espacio

Estimada/o [nombre]:

La autenticación se completa correctamente, por lo que el problema no corresponde al acceso general a PRADO.

Necesitamos que nos indique el nombre de la asignatura o espacio docente, el curso académico y la titulación para comprobar su incorporación.

Un saludo.

## Categorías de IRIS relacionadas

- [Acceso](/prado/iris/acceso.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Sin resolver](/prado/iris/sin-resolver.md)

## Conceptos relacionados

- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso o verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [Docente externo](/prado/usuarios-y-roles/docente-externo.md)
