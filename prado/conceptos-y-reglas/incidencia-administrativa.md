---
type: Rule
title: Incidencia administrativa
description: Regla para identificar y tratar los bloqueos administrativos que impiden al alumnado acceder a PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - incidencia-administrativa
  - acceso
  - alumnado
  - oficina-virtual
  - idp
---

# Incidencia administrativa

## Definición

Existe una incidencia administrativa cuando el expediente de un estudiante está bloqueado por una causa gestionada desde la secretaría del centro.

La documentación interna señala que esta situación suele estar relacionada con problemas de pago de matrícula, aunque la causa concreta debe confirmarse en cada caso.

Mientras el bloqueo permanece activo, el alumnado puede no poder acceder a PRADO.

## Cómo comprobarla

La comprobación principal debe realizarse mediante la:

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](consulta-estado-acceso-prado.md).

Esta consulta permite revisar:

- si existe una incidencia administrativa;
- el centro o centros responsables;
- la situación registrada por la secretaría;
- si el expediente ya ha sido desbloqueado.

## Diferencia entre Oficina Virtual e IdP

La información no se actualiza al mismo tiempo en todos los sistemas.

### Oficina Virtual

- refleja la información grabada por las secretarías;
- puede mostrar de forma inmediata que la incidencia ha sido retirada;
- permite identificar el centro al que debe dirigirse el estudiante.

### Proveedor de identidad —IdP—

El atributo de incidencia administrativa recibido mediante el [Proveedor de identidad —IdP—](proveedor-identidad-idp.md) puede tardar en actualizarse.

Como referencia operativa interna:

- se informa de un plazo de hasta 24 horas;
- el refresco puede realizarse una vez por la mañana y otra por la tarde.

Por tanto, puede ocurrir que Oficina Virtual muestre el expediente desbloqueado mientras PRADO todavía conserva temporalmente el estado anterior.

## Caché de acceso

PRADO puede conservar temporalmente en caché la información recibida del IdP.

Cuando la incidencia ya ha sido retirada en Oficina Virtual, pero el acceso sigue bloqueado, puede ser necesario revisar internamente:

- cuándo se actualizó el atributo;
- el último estado recibido por la plataforma;
- el último control realizado por PRADO;
- si ya ha transcurrido el plazo de actualización.

Las herramientas técnicas internas y sus direcciones no deben incluirse en las respuestas a las personas usuarias.

## Comprobaciones del CAU

Ante una posible incidencia administrativa:

1. confirmar la identidad y el correo institucional;
2. comprobar la plataforma afectada;
3. revisar la Consulta de Estado para Acceso a PRADO;
4. comprobar si aparece una incidencia administrativa;
5. identificar el centro o centros responsables;
6. verificar si la secretaría ya ha desbloqueado el expediente;
7. comparar la información con el IdP;
8. comprobar si existe un retraso de actualización o caché;
9. aplicar el plazo correspondiente antes de escalar.

## Árbol de decisión

### Caso 1. La incidencia administrativa sigue activa

1. informar de que el acceso está bloqueado por una causa administrativa;
2. indicar el centro responsable;
3. remitir al estudiante a la secretaría correspondiente;
4. no intentar resolver el bloqueo desde PRADO;
5. clasificar el ticket como `Incidencia administrativa`.

### Caso 2. La incidencia ya no aparece en Oficina Virtual

1. comprobar cuándo fue retirada;
2. tener en cuenta el retraso del IdP y la caché de PRADO;
3. esperar el plazo de actualización aplicable;
4. pedir al estudiante que pruebe de nuevo;
5. revisar o escalar si el problema continúa después del plazo.

### Caso 3. Aparecen dos centros responsables

1. informar al estudiante de los dos centros;
2. indicar que debe contactar con ambos;
3. mantener el ticket pendiente hasta que se aclare la situación administrativa.

### Caso 4. No existe incidencia administrativa

1. descartar esta causa;
2. comprobar matrícula, autenticación y participación;
3. aplicar el procedimiento específico;
4. reclasificar el ticket según la causa comprobada.

### Caso 5. La consulta afecta a Posgrado

1. no basar la conclusión únicamente en Oficina Virtual;
2. comprobar la matrícula mediante las [vistas de bases de datos](vistas-bases-datos.md);
3. revisar la información del IdP y de PRADO;
4. clasificar según el resultado.

## Diferencia con otras categorías

### Incidencia administrativa

Existe un bloqueo del expediente gestionado por la secretaría.

### Acceso

La situación administrativa es correcta, pero la persona no puede autenticarse o entrar en la plataforma.

### Matrícula

La persona no consta oficialmente en una asignatura.

### Sin resolver

No se ha podido determinar la causa después de completar las comprobaciones.

## Plantillas de respuesta

### Plantilla 1. Incidencia administrativa activa

Estimada/o [nombre]:

Hemos comprobado que existe una incidencia administrativa asociada a su expediente que está impidiendo el acceso a PRADO.

Debe contactar con la secretaría del centro que aparece en el apartado **«Consulta de Estado para Acceso a PRADO»** de su Oficina Virtual.

Desde PRADO no podemos modificar ni retirar este bloqueo administrativo.

Un saludo.

---

### Plantilla 2. La incidencia ya se ha retirado

Estimada/o [nombre]:

En la Oficina Virtual ya no aparece activa la incidencia administrativa.

No obstante, la actualización de esta información en los sistemas de acceso a PRADO puede demorarse. Le recomendamos que vuelva a probar el acceso después de transcurridas hasta 24 horas desde que la secretaría regularizó su expediente.

Si después de ese plazo el problema continúa, responda a este ticket para que podamos revisarlo nuevamente.

Un saludo.

---

### Plantilla 3. Aparecen dos centros

Estimada/o [nombre]:

En la Consulta de Estado para Acceso a PRADO aparecen dos centros relacionados con su situación administrativa.

Debe contactar con las secretarías de ambos centros para que puedan determinar cuál debe regularizar el expediente.

Una vez resuelta la incidencia, la actualización del acceso a PRADO puede no ser inmediata.

Un saludo.

## Conceptos relacionados

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](consulta-estado-acceso-prado.md)
- [Proveedor de identidad —IdP—](proveedor-identidad-idp.md)
- [Vistas de bases de datos](vistas-bases-datos.md)
- [Plazos de sincronización y actualización](plazos-sincronizacion.md)

## Procedimientos relacionados

- Comprobación del estado de acceso
- [Problemas de acceso o verificación en dos pasos](../procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- El alumnado está matriculado, pero no puede ver el curso

## Categorías de IRIS relacionadas

- Incidencia administrativa
- Acceso
- Matrícula
- Sin resolver
