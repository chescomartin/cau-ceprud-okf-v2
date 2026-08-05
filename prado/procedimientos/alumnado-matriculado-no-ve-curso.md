---
type: Procedure
title: El alumnado está matriculado, pero no puede ver el curso
description: Procedimiento para comprobar por qué un estudiante que afirma estar matriculado no ve una asignatura o espacio en PRADO.
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
  - prado
  - alumnado
  - matricula
  - visibilidad
  - participacion
  - sincronizacion
---

# El alumnado está matriculado, pero no puede ver el curso

## Objetivo

Determinar por qué un estudiante que afirma estar matriculado no ve una asignatura o espacio docente en PRADO.

La comprobación debe distinguir entre:

- ausencia o error en la matrícula oficial;
- retraso de sincronización;
- cambio de grupo;
- participación suspendida;
- participación no activa;
- curso oculto;
- problema general de acceso;
- asimilación entre asignaturas o grupos;
- error del automatismo.

## Datos que deben solicitarse

Antes de realizar comprobaciones, solicitar:

- nombre y apellidos;
- correo institucional;
- plataforma:
  - PRADO Grado;
  - PRADO Posgrado;
- curso académico;
- nombre de la asignatura;
- código de asignatura, cuando se conozca;
- grupo;
- titulación;
- explicación concreta del problema;
- captura de pantalla, cuando sea posible.

## Pregunta inicial

Comprobar primero:

> ¿El estudiante puede entrar en PRADO y lo único que falta es una asignatura o curso concreto?

- Si no puede entrar en la plataforma, aplicar [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md).
- Si puede entrar, continuar con la revisión de matrícula, participación y visibilidad.

## Procedimiento

### Paso 1. Comprobar la matrícula oficial

En PRADO Grado, revisar la:

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md).

En PRADO Posgrado, consultar las:

- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md).

Comprobar:

- que la asignatura consta;
- que corresponde al curso académico;
- que el grupo es correcto;
- que no existe una incidencia administrativa;
- que los datos identificativos coinciden.

### Paso 2. Interpretar el resultado de matrícula

#### La asignatura no consta oficialmente

No debe realizarse una [matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md) como solución ordinaria.

Actuación:

1. informar de que PRADO recibe la matrícula desde las fuentes oficiales;
2. remitir al estudiante a la secretaría de su centro;
3. clasificar el ticket como [Matrícula](/prado/iris/matricula.md).

#### La asignatura consta correctamente

Continuar con las comprobaciones de sincronización, participación y visibilidad.

### Paso 3. Comprobar la fecha de la matrícula o modificación

Revisar cuándo se registró:

- el alta de matrícula;
- el cambio de grupo;
- la anulación o recuperación de matrícula;
- la corrección administrativa.

Aplicar los:

- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md).

Si la modificación es reciente, debe esperarse a que los automatismos procesen la información.

### Paso 4. Comprobar la participación en PRADO

Buscar al estudiante en la relación de participantes del espacio y comprobar si aparece como:

- activo;
- [participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md);
- [participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md);
- incorporado manualmente;
- ausente.

#### Participación suspendida

La persona dejó de llegar desde la fuente oficial.

Comprobar:

- si se produjo una baja;
- si hubo un cambio de grupo;
- si existe una participación activa en otro espacio;
- si está pendiente una [baja automática](/prado/conceptos-y-reglas/bajas-automaticas.md).

No debe reactivarse manualmente sin comprobar el origen.

#### Participación no activa

Comprobar si fue añadida manualmente al margen de la matrícula oficial.

La solución debe consistir en corregir la matrícula en origen, no en mantener de forma permanente la participación manual.

#### No existe participación

Si la matrícula consta correctamente:

1. comprobar las vistas de bases de datos;
2. confirmar que ya ha transcurrido el plazo de actualización;
3. revisar el grupo y el código de asignatura;
4. comprobar si existe una asimilación;
5. escalar si el automatismo no ha generado la participación.

### Paso 5. Comprobar el grupo

Verificar que el estudiante consulta el espacio correspondiente a su grupo oficial.

Debe tenerse en cuenta que:

- un cambio reciente puede dejar temporalmente visible el grupo anterior;
- el estudiante puede estar ya activo en el nuevo grupo;
- una asimilación puede hacer que el grupo mostrado en PRADO no coincida literalmente con el consultado en la secretaría.

Consultar, cuando proceda:

- [Asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md);
- [Código de asignatura](/prado/conceptos-y-reglas/codigo-asignatura.md).

### Paso 6. Comprobar la visibilidad del curso

Si la matrícula y la participación son correctas, comprobar si el curso está oculto desde el punto de vista del estudiante.

Cuando el curso está configurado como oculto:

- el profesorado puede verlo;
- el alumnado puede tener una participación correcta, pero no verlo;
- la incidencia debe clasificarse como `Visibilidad`.

La publicación del curso corresponde al profesorado o a la persona con permisos suficientes en el espacio.

### Paso 7. Comprobar el curso académico y el Área personal

Confirmar que el estudiante está consultando:

- el curso académico correcto;
- la plataforma correcta;
- los apartados correspondientes de su Área personal.

Revisar si el curso aparece en otra clasificación temporal, como futuros o en progreso.

### Paso 8. Clasificar el ticket

Seleccionar la categoría según la causa comprobada:

- [Matrícula](/prado/iris/matricula.md): la matrícula falta, es incorrecta o no se ha reflejado;
- [Baja de usuario](/prado/iris/baja-usuario.md): existe una baja o cambio de grupo pendiente;
- [Gestión manual](/prado/iris/gestion-manual.md): la incidencia deriva de una incorporación manual;
- [Asimilaciones docentes](/prado/iris/asimilaciones-docentes.md): la causa es una asimilación;
- `Visibilidad`: la participación es correcta, pero el curso está oculto;
- [Acceso](/prado/iris/acceso.md): el estudiante no puede entrar en PRADO;
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md): existe un bloqueo administrativo;
- `Sin resolver`: no se identifica la causa después de las comprobaciones.

## Árbol de decisión resumido

### No puede entrar en PRADO

Aplicar:

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md).

### Puede entrar, pero la asignatura no consta en matrícula

- remitir a secretaría;
- categoría `Matrícula`;
- no realizar alta manual ordinaria.

### La matrícula consta, pero el cambio es reciente

- aplicar los plazos de sincronización;
- volver a comprobar después del plazo.

### La participación está suspendida

- comprobar baja o cambio de grupo;
- categoría `Baja de usuario` o `Matrícula`, según la causa.

### La participación está no activa

- comprobar incorporación manual;
- categoría `Gestión manual` o `Matrícula`.

### La participación está activa, pero el curso está oculto

- categoría `Visibilidad`;
- indicar que el profesorado debe publicar el curso.

### Todo consta correctamente y el curso sigue sin aparecer

- revisar grupo, código y asimilaciones;
- comprobar los automatismos;
- escalar la incidencia.

## Transferencia del ticket

La transferencia relacionada con matrícula debe valorarse únicamente después de realizar las comprobaciones disponibles.

Puede considerarse cuando:

- el estudiante afirma haber acudido a la secretaría;
- la información continúa siendo contradictoria;
- el CEPRUD no puede resolver la causa;
- la unidad de destino puede comprobar o corregir la matrícula en origen.

Debe tenerse en cuenta que una transferencia puede impedir que el CEPRUD recupere posteriormente la gestión del ticket.

## Qué no debe hacerse

No debe:

- añadirse manualmente al estudiante como solución ordinaria;
- atribuirse automáticamente el problema a `Acceso`;
- indicarse que el curso está oculto sin comprobarlo;
- reactivarse una participación suspendida sin revisar la fuente oficial;
- ignorarse el grupo o el curso académico;
- confundirse matrícula con asignación docente;
- prometer una actualización inmediata.

## Plantillas de respuesta

### Plantilla 1. La matrícula no consta

Estimada/o [nombre]:

La asignatura indicada no consta actualmente en la información oficial de matrícula que recibe PRADO.

Debe contactar con la secretaría de su centro para revisar la matrícula. Cuando la información quede registrada correctamente, el alta se reflejará en PRADO mediante los procesos automáticos.

Un saludo.

---

### Plantilla 2. Matrícula reciente

Estimada/o [nombre]:

La matrícula o modificación indicada se ha registrado recientemente y su reflejo en PRADO puede no ser inmediato.

Le recomendamos que vuelva a comprobarlo cuando haya transcurrido el plazo habitual de actualización. No es conveniente realizar una incorporación manual mientras el cambio oficial está pendiente de sincronización.

Un saludo.

---

### Plantilla 3. Curso oculto

Estimada/o [nombre]:

La matrícula y la participación en la asignatura constan correctamente, pero el curso se encuentra oculto para el alumnado.

La publicación del espacio corresponde al profesorado responsable del curso.

Un saludo.

---

### Plantilla 4. Incidencia técnica pendiente de revisión

Estimada/o [nombre]:

La matrícula consta correctamente y ya ha transcurrido el plazo habitual de actualización.

Vamos a revisar por qué la participación o el curso no se muestran correctamente en PRADO.

Un saludo.

## Conceptos relacionados

- [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md)
- [Código de asignatura](/prado/conceptos-y-reglas/codigo-asignatura.md)
- [Transferencia de tickets en IRIS](/prado/conceptos-y-reglas/transferencia-tickets-iris.md)

## Estados relacionados

- [Participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md)
- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)

## Categorías de IRIS relacionadas

- [Matrícula](/prado/iris/matricula.md)
- [Baja de usuario](/prado/iris/baja-usuario.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Asimilaciones docentes](/prado/iris/asimilaciones-docentes.md)
- [Acceso](/prado/iris/acceso.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [Visibilidad](/prado/iris/visibilidad.md)
- [Sin resolver](/prado/iris/sin-resolver.md)
