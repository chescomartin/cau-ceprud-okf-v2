---
type: Rule
title: Transferencia de tickets en IRIS
description: Regla operativa para valorar y ejecutar la transferencia de tickets de PRADO a otros servicios o secretarías de centro mediante IRIS.
service: PRADO
system: IRIS
audience: personal-cau
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - iris
  - transferencia
  - tickets
  - secretarias
  - escalado
  - cau
---

# Transferencia de tickets en IRIS

## Definición

La **transferencia de un ticket en IRIS** consiste en trasladar su titularidad desde el CEPRUD a otro servicio o a una secretaría de centro cuando la unidad de destino debe comprobar, autorizar o corregir información que el CEPRUD no puede resolver directamente.

La transferencia no debe utilizarse como sustituto de las comprobaciones previas ni como una forma ordinaria de derivar incidencias cuya causa todavía no se ha identificado.

## Destinos disponibles

IRIS permite transferir tickets a:

- determinados servicios de la Universidad;
- las secretarías de los centros disponibles en el sistema.

No aparecen como destinos las secretarías de los departamentos.

La documentación interna indica que debe seleccionarse el destino de nivel jerárquico superior que corresponda. En el caso del CEPRUD, la referencia indicada es:

- `CEPRUD/Centro`.

## Criterio general de decisión

La decisión de transferir debe valorarla el personal técnico según:

- la causa comprobada;
- las actuaciones ya realizadas;
- la evolución de la incidencia;
- la unidad que tiene capacidad para consultar o modificar la información en origen;
- y las consecuencias de perder la titularidad del ticket.

Antes de transferir debe quedar claro:

1. qué se ha comprobado;
2. qué información resulta contradictoria o incorrecta;
3. por qué el CEPRUD no puede resolverla;
4. qué actuación se solicita a la unidad de destino;
5. qué respuesta se ha dado hasta ese momento a la persona usuaria.

## Casos candidatos a transferencia

### Matrícula

Puede valorarse la transferencia cuando:

1. se han realizado todas las comprobaciones disponibles;
2. la persona afirma haber acudido previamente a la secretaría;
3. la información continúa siendo contradictoria;
4. el CEPRUD no puede corregir la matrícula en origen;
5. la secretaría del centro es la unidad que puede revisar o modificar los datos oficiales.

Antes de transferir deben revisarse:

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md), en Grado;
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md);
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md);
- [Matrícula](/prado/iris/matricula.md);
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md).

### Ordenación docente

La documentación interna contempla la transferencia por `Ordenación docente` únicamente para determinados casos de la Escuela Internacional de Posgrado —EIP—, ya que su secretaría gestiona la asignación docente correspondiente.

Antes de transferir deben comprobarse:

- la asignación oficial;
- el grupo;
- el tipo de docencia;
- el curso académico;
- y que la unidad de destino sea realmente responsable de corregir el dato.

Consultar:

- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md);
- [Ordenación docente](/prado/iris/ordenacion-docente.md);
- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md).

### Solicitud de autorización a Ordenación Académica

Cuando una actuación manual requiere el visto bueno de Ordenación Académica:

1. el ticket puede transferirse para solicitar la autorización;
2. la autorización debe quedar por escrito en el propio ticket;
3. la unidad debe devolver el ticket con la conformidad correspondiente;
4. solo entonces debe realizarse la actuación autorizada.

Consultar:

- [Alta manual de un docente con autorización de Ordenación Académica](/prado/procedimientos/alta-manual-autorizacion-ordenacion-academica.md);
- [Gestión manual](/prado/iris/gestion-manual.md).

## Comprobaciones antes de transferir

Antes de ejecutar la transferencia:

1. confirmar la identidad de la persona afectada;
2. identificar con precisión la plataforma, el curso académico, la asignatura y el grupo;
3. comprobar la categoría de IRIS correspondiente;
4. revisar las fuentes oficiales disponibles;
5. aplicar los plazos de sincronización;
6. comprobar que la unidad de destino tiene competencia sobre el dato;
7. documentar todas las actuaciones realizadas;
8. redactar claramente qué se solicita a la unidad receptora;
9. informar a la persona usuaria cuando proceda;
10. valorar si la transferencia es necesaria teniendo en cuenta que el CEPRUD no podrá recuperar después la titularidad.

## Consecuencias de la transferencia

Una vez transferido el ticket:

- el CEPRUD deja de ser su propietario;
- el personal técnico del CEPRUD no puede recuperarlo directamente;
- tampoco puede cerrarlo mientras la titularidad corresponda a la unidad receptora;
- la actividad posterior puede notificarse únicamente mediante correo electrónico;
- la unidad de destino pasa a ser responsable de su gestión.

Por este motivo, la transferencia debe realizarse únicamente cuando esté justificada y correctamente documentada.

## Transferencia con marca de departamento

La documentación interna advierte que una transferencia realizada con marca de departamento:

- tampoco permite recuperar el ticket;
- puede hacer que todos los técnicos del CEPRUD lo vean;
- puede generar confusión sobre quién lo está gestionando;
- no permite al CEPRUD cerrarlo porque el propietario continúa siendo el servicio receptor.

Debe evitarse utilizar esta opción sin comprender previamente su efecto.

## Qué debe incluir la nota de transferencia

La nota dirigida a la unidad receptora debe indicar:

- resumen de la incidencia;
- datos necesarios para identificar el caso;
- comprobaciones realizadas;
- resultados obtenidos;
- fecha de las modificaciones relevantes;
- plazo de actualización ya transcurrido;
- contradicción o dato que debe revisarse;
- actuación concreta que se solicita;
- respuesta facilitada a la persona usuaria.

No deben incluirse datos personales o documentación sensible que no sean necesarios para resolver el ticket.

## Qué no debe hacerse

No debe:

- transferirse un ticket sin haber realizado las comprobaciones disponibles;
- elegirse el destino únicamente por la descripción inicial de la persona usuaria;
- transferirse a una unidad que no puede modificar el dato en origen;
- utilizarse la transferencia para evitar clasificar el ticket;
- enviarse un caso de matrícula antes de revisar la información oficial y los plazos;
- transferirse por ordenación docente fuera de los supuestos internos previstos;
- asumirse que el CEPRUD podrá recuperar o cerrar después el ticket;
- utilizarse la marca de departamento sin valorar sus consecuencias;
- enviarse una nota sin explicar qué actuación se solicita.

## Resultado esperado

Antes de ejecutar la transferencia debe quedar identificado:

- la causa comprobada;
- la categoría de IRIS;
- la unidad competente;
- las comprobaciones realizadas;
- el motivo por el que el CEPRUD no puede resolver el caso;
- la actuación solicitada;
- y la aceptación de que la titularidad del ticket dejará de corresponder al CEPRUD.

## Modelo de nota interna

**Comprobaciones realizadas**

- Persona afectada: [nombre y correo institucional].
- Plataforma: [PRADO Grado / PRADO Posgrado].
- Curso académico: [curso].
- Asignatura y grupo: [datos].
- Categoría: [categoría de IRIS].
- Fuentes consultadas: [Oficina Virtual / vistas / IdP / PRADO].
- Resultado: [resumen].
- Fecha de la modificación: [fecha].
- Plazo transcurrido: [plazo].

**Motivo de la transferencia**

[Explicar por qué el CEPRUD no puede resolver el caso y qué dato debe comprobar o corregir la unidad receptora].

**Actuación solicitada**

[Indicar de forma concreta qué debe revisar, autorizar o modificar la unidad de destino].

## Plantilla de respuesta a la persona usuaria

Estimada/o [nombre]:

Hemos realizado las comprobaciones disponibles desde el CEPRUD. Para continuar con la revisión es necesario que la unidad responsable compruebe la información registrada en origen.

Hemos trasladado su incidencia a [servicio o secretaría], que continuará con su gestión.

Un saludo.

## Conceptos relacionados

- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)

## Procedimientos relacionados

- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [Alta manual de un docente con autorización de Ordenación Académica](/prado/procedimientos/alta-manual-autorizacion-ordenacion-academica.md)

## Categorías de IRIS relacionadas

- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [Sin resolver](/prado/iris/sin-resolver.md)
