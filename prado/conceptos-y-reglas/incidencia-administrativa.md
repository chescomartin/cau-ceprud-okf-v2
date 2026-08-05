---
type: Rule
title: Incidencia administrativa
description: Qué es un bloqueo administrativo del expediente, por qué impide el acceso a PRADO y cómo se comprueba.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-09-05
last_reviewed: 2026-08-05
synonyms:
  - expediente bloqueado
  - bloqueo administrativo
  - no puedo entrar por un problema de matrícula
tags:
  - prado
  - incidencia-administrativa
  - acceso
  - alumnado
  - oficina-virtual
---

# Incidencia administrativa

> **Alcance de este documento.** Aquí se explica **qué es** una incidencia administrativa,
> **por qué** impide el acceso y **cómo se comprueba**.
>
> - Para **clasificar el ticket**: [IRIS: Incidencia administrativa](/prado/iris/incidencia-administrativa.md).
> - Para **responder a la persona usuaria**: [respuestas tipo](/respuestas-tipo/index.md) RT-001 a RT-003.

## Definición

Existe una incidencia administrativa cuando el expediente de un estudiante está bloqueado
por una causa gestionada desde la **secretaría del centro**.

Mientras el bloqueo permanece activo, el alumnado puede no poder acceder a PRADO.

La documentación interna señala que esta situación suele estar relacionada con problemas
de pago de matrícula, **aunque la causa concreta debe confirmarse en cada caso** y no debe
comunicarse como un hecho sin haberla verificado.

## Por qué impide el acceso

PRADO no consulta directamente el expediente. Recibe la situación administrativa como un
**atributo** a través del [proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md). Si
ese atributo indica que existe una incidencia, la plataforma deniega el acceso.

De ahí se derivan las dos características que explican casi todas las consultas:

1. **El CEPRUD no puede retirar el bloqueo.** Solo puede hacerlo la secretaría competente,
   en el sistema de origen.
2. **La retirada no surte efecto de forma inmediata.** El atributo tarda en actualizarse y
   PRADO puede conservar temporalmente el valor anterior en caché.

## Cómo se comprueba

La comprobación principal se realiza mediante la
[Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md),
que permite revisar:

- si existe una incidencia administrativa;
- el centro o centros responsables;
- la situación registrada por la secretaría;
- si el expediente ya ha sido desbloqueado.

### Comprobaciones del CAU

1. Confirmar la identidad y el correo institucional.
2. Comprobar la plataforma afectada.
3. Revisar la Consulta de Estado para Acceso a PRADO.
4. Comprobar si aparece una incidencia administrativa.
5. Identificar el centro o centros responsables.
6. Verificar si la secretaría ya ha desbloqueado el expediente.
7. Comparar la información con la recibida del IdP.
8. Comprobar si existe un retraso de actualización o caché.
9. Aplicar el plazo correspondiente antes de escalar.

## Desfase entre sistemas

La información no se actualiza al mismo tiempo en todos los sistemas.

| Sistema | Comportamiento |
|---|---|
| **Oficina Virtual** | Refleja lo grabado por las secretarías. Puede mostrar de forma inmediata que la incidencia ha sido retirada. Permite identificar el centro. |
| **Proveedor de identidad —IdP—** | El atributo puede tardar en actualizarse. |
| **PRADO** | Puede conservar temporalmente en caché el último valor recibido del IdP. |

El plazo aplicable y la frecuencia de refresco se consultan en
[Parámetros operativos de PRADO](/prado/parametros-operativos.md).

**Consecuencia práctica:** puede ocurrir que Oficina Virtual muestre el expediente
desbloqueado mientras PRADO todavía conserva el estado anterior. No es un fallo.

### Cuando el bloqueo persiste tras el plazo

Si la incidencia ya se retiró en Oficina Virtual y, transcurrido el plazo, el acceso sigue
bloqueado, debe revisarse internamente:

- cuándo se actualizó el atributo;
- el último estado recibido por la plataforma;
- el último control realizado por PRADO;
- si ya ha transcurrido el plazo de actualización.

> **Restricción.** Las herramientas técnicas internas y sus direcciones **no deben
> incluirse en las respuestas a las personas usuarias**.

## Caso particular: Posgrado

En Posgrado no debe basarse la conclusión únicamente en Oficina Virtual. Es necesario
comprobar además la matrícula mediante las
[vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md) y contrastar la información del IdP y de
PRADO antes de determinar la causa.

## Caso particular: dos centros responsables

Cuando la consulta muestra dos centros —situación habitual en dobles grados y en cambios
de centro— y no puede determinarse cuál es el competente, el estudiante debe dirigirse a
ambos y el ticket se mantiene pendiente hasta que se aclare.

## Qué NO cubre esta regla

| Situación | Documento aplicable |
|---|---|
| La situación administrativa es correcta pero la persona no puede autenticarse | [IRIS: Acceso](/prado/iris/acceso.md) |
| La persona no consta oficialmente matriculada | [IRIS: Matrícula](/prado/iris/matricula.md) |
| Entra en PRADO pero no ve una asignatura | [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md) |
| No se determina la causa tras las comprobaciones | [IRIS: Sin resolver](/prado/iris/sin-resolver.md) |

## Conceptos relacionados

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Oficina Virtual](/prado/conceptos-y-reglas/oficina-virtual.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Parámetros operativos de PRADO](/prado/parametros-operativos.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso o verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
