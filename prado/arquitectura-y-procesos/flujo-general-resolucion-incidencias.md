---
type: KnowledgeDocument
title: Flujo general de resolución de incidencias de PRADO
description: Secuencia operativa para identificar, comprobar, clasificar, resolver o transferir incidencias de PRADO.
service: PRADO
status: draft
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - arquitectura
  - procesos
  - tickets
  - resolucion-incidencias
---

# Flujo general de resolución de incidencias de PRADO

## Naturaleza de este documento

Este flujo es una **síntesis operativa** construida a partir de las definiciones, reglas, categorías y procedimientos disponibles en la base de conocimiento.

La documentación fuente no contiene todavía un flujo general completo y ordenado. Por tanto, esta ficha deberá revisarse cuando se apruebe un procedimiento institucional único.

## Objetivo

El flujo pretende que el personal técnico pueda:

1. identificar correctamente el contexto;
2. comprobar los datos en la fuente adecuada;
3. distinguir un error real de un retraso de actualización;
4. clasificar el ticket;
5. realizar la actuación que corresponda;
6. transferirlo únicamente cuando no pueda resolverse desde el CEPRUD;
7. dejar constancia de las comprobaciones realizadas.

# Fase 1: identificar el contexto

## 1. Plataforma

Determinar dónde se produce la incidencia:

- PRADO Grado;
- PRADO Posgrado;
- E-CAMPUS;
- ABIERTA UGR;
- otra plataforma.

No deben aplicarse automáticamente las mismas fuentes y reglas a todas las plataformas.

Por ejemplo:

- la consulta de matrícula de Oficina Virtual resulta útil para Grado;
- en Posgrado debe recurrirse a las vistas de bases de datos.

## 2. Curso académico

Comprobar:

- el curso académico al que se refiere la persona;
- el curso que está consultando en PRADO;
- y el año académico de los atributos del proveedor de identidad.

Una incidencia puede deberse a que se está consultando el curso anterior o el siguiente.

## 3. Persona afectada

Registrar:

- nombre;
- correo institucional;
- número identificativo, cuando sea necesario;
- condición de alumno, docente, coordinación o usuario externo;
- cuenta utilizada para acceder.

Consultar:

- [Usuarios y roles](../usuarios-y-roles/index.md)

## 4. Espacio afectado

Identificar:

- nombre;
- código;
- tipo de espacio;
- asignatura o titulación;
- grupo;
- plataforma.

Consultar:

- [Espacios docentes](../espacios-docentes/index.md)
- [Código de asignatura](../conceptos-y-reglas/codigo-asignatura.md)

# Fase 2: concretar la incidencia

## 5. Describir el comportamiento

Distinguir entre situaciones como:

- no puede autenticarse;
- entra en la plataforma, pero no ve el curso;
- aparece con un rol incorrecto;
- falta alumnado;
- falta profesorado;
- aparece una participación suspendida;
- aparece una participación no activa;
- el curso está oculto;
- existe una cuenta o un rol duplicado;
- se solicita una incorporación manual;
- se solicita crear o modificar un espacio docente.

La descripción debe indicar:

- qué esperaba encontrar la persona;
- qué encuentra realmente;
- desde cuándo ocurre;
- y qué cambios administrativos ha realizado.

## 6. Seleccionar la categoría de IRIS

Elegir el tema de ayuda que describa mejor la causa o el ámbito principal.

Consultar:

- [Categorías de IRIS](../iris/index.md)

Debe prestarse especial atención a distinciones como:

- [Acceso](../iris/acceso.md) frente a [Incidencia administrativa](../iris/incidencia-administrativa.md);
- [Matrícula](../iris/matricula.md) frente a [Ordenación docente](../iris/ordenacion-docente.md);
- [Gestión manual](../iris/gestion-manual.md) frente a altas procedentes de fuentes oficiales;
- [Visibilidad](../iris/visibilidad.md) frente a ausencia real de participación.

IRIS solo permite seleccionar un tema de ayuda, por lo que debe elegirse el que mejor represente el problema principal.

# Fase 3: consultar la fuente adecuada

## 7. Incidencias del alumnado

Cuando el problema afecta a la presencia de un estudiante, comprobar:

- matrícula oficial;
- grupo;
- incidencia administrativa;
- curso académico;
- estado de la participación;
- visibilidad del espacio.

Fuentes habituales:

### Grado

- Oficina Virtual;
- Consulta de Estado para Acceso a PRADO;
- vistas de bases de datos.

### Posgrado

- vistas de bases de datos;
- atributos del IdP cuando el problema sea de acceso.

No debe utilizarse la consulta de matrícula de Oficina Virtual como fuente principal para Posgrado.

## 8. Incidencias del profesorado

Cuando el problema afecta a una persona docente, comprobar:

- Plan de Ordenación Docente;
- asignatura;
- grupo;
- créditos;
- curso académico;
- rol y estado de la participación.

Fuentes habituales:

- POD;
- vistas de bases de datos;
- información institucional de Ordenación Académica.

## 9. Incidencias de acceso

Comprobar:

- cuenta utilizada;
- dominio del correo;
- proveedor de identidad;
- atributos del curso académico;
- incidencia administrativa;
- caché de acceso;
- verificación en dos pasos, cuando corresponda.

Consultar:

- [Comprobación del estado de acceso](../procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso con verificación en dos pasos](../procedimientos/problemas-acceso-verificacion-dos-pasos.md)

## 10. Incidencias de espacios docentes

Comprobar:

- tipo de espacio;
- reglas de creación;
- código;
- participantes que deben incorporarse automáticamente;
- persona responsable;
- visibilidad;
- posibles altas manuales.

Consultar:

- [Espacios docentes](../espacios-docentes/index.md)

# Fase 4: interpretar los datos

## 11. Comparar la fuente oficial con PRADO

Determinar si:

- la información oficial es correcta y PRADO aún no se ha actualizado;
- la información oficial no contiene a la persona;
- PRADO conserva una participación anterior;
- existe una incorporación manual;
- hay una cuenta duplicada;
- el espacio está oculto;
- o se está consultando la plataforma, el curso o el código equivocados.

## 12. Revisar los plazos

Antes de realizar una modificación manual, comprobar:

- cuándo se registró el cambio en la fuente oficial;
- qué automatismo debe ejecutarse;
- y si ha transcurrido el plazo correspondiente.

Consultar:

- [Plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md)
- [Altas automáticas](../conceptos-y-reglas/altas-automaticas.md)
- [Bajas automáticas](../conceptos-y-reglas/bajas-automaticas.md)

No debe corregirse manualmente una situación que todavía está dentro de su plazo normal de actualización, salvo que exista un procedimiento específico que lo autorice.

# Fase 5: decidir la actuación

## 13. Resolver desde el CEPRUD

Procede resolver cuando:

- las comprobaciones identifican una actuación técnica competencia del CEPRUD;
- existe un procedimiento documentado;
- y se dispone de la información o autorización necesaria.

Consultar:

- [Procedimientos](../procedimientos/index.md)

## 14. Informar y esperar

Procede informar del plazo cuando:

- el cambio ya figura en la fuente oficial;
- el automatismo todavía no se ha ejecutado;
- y no existe una urgencia o excepción documentada.

Debe indicarse:

- qué cambio se está esperando;
- desde qué fecha;
- y cuándo debería revisarse de nuevo.

## 15. Solicitar una corrección administrativa

Cuando la información oficial es incorrecta o incompleta, la persona debe dirigirse a la unidad que gestiona el dato.

Ejemplos:

- matrícula: secretaría del centro;
- asignación docente: departamento u Ordenación Académica, según el caso;
- coordinación de titulación: unidad responsable de su registro institucional.

PRADO no debe utilizarse para sustituir o contradecir de forma permanente la información oficial.

## 16. Realizar una actuación manual autorizada

Las altas o cambios manuales deben limitarse a los supuestos documentados.

Antes de actuar, registrar:

- quién solicita la actuación;
- la justificación;
- la autorización;
- el rol;
- el espacio;
- y el resultado.

Consultar:

- [Gestión manual](../iris/gestion-manual.md)
- [Matrícula manual](../conceptos-y-reglas/matricula-manual.md)

## 17. Transferir el ticket

La transferencia debe valorarse después de realizar las comprobaciones disponibles.

Puede ser candidata a transferencia una incidencia de matrícula cuando:

- se han realizado las comprobaciones;
- el estudiante afirma haber acudido a su secretaría;
- y el CEPRUD no puede resolver el problema.

En Ordenación docente, la documentación interna limita la transferencia a los casos de la EIP en los que esta unidad gestiona la asignación.

Consultar:

- [Transferencia de tickets en IRIS](../conceptos-y-reglas/transferencia-tickets-iris.md)

## Advertencia sobre la transferencia

Una vez transferido el ticket:

- el CEPRUD deja de ser su propietario;
- no puede recuperarlo;
- y no puede cerrarlo.

Por esta razón, la transferencia no debe emplearse como sustituto de las comprobaciones técnicas previas.

# Fase 6: documentar el resultado

## 18. Registrar las comprobaciones

Dejar constancia de:

- plataforma;
- curso académico;
- persona;
- correo;
- código del espacio;
- matrícula o asignación consultada;
- fuente utilizada;
- rol y estado;
- fechas relevantes;
- plazos;
- actuación realizada;
- unidad a la que se remite, cuando corresponda.

## 19. Redactar la respuesta

La respuesta debe explicar:

- qué se ha comprobado;
- cuál es la causa identificada;
- qué actuación se ha realizado;
- qué debe hacer la persona;
- y qué plazo debe tener en cuenta.

## 20. Cerrar o transferir

### Cierre

Cerrar cuando:

- la incidencia está resuelta;
- se ha facilitado la información necesaria;
- o la actuación depende ahora de una gestión que corresponde al usuario ante otra unidad y no procede la transferencia.

### Transferencia

Transferir únicamente cuando:

- la unidad de destino está disponible en IRIS;
- tiene competencia sobre el dato o la actuación;
- y se han documentado las comprobaciones previas.

# Resumen del flujo

```text
Identificar plataforma, curso, persona y espacio
        ↓
Concretar el problema
        ↓
Elegir la categoría de IRIS
        ↓
Consultar la fuente oficial adecuada
        ↓
Comparar la fuente con PRADO
        ↓
Comprobar plazos y automatismos
        ↓
Resolver / informar y esperar / solicitar corrección / actuar manualmente / transferir
        ↓
Documentar y responder
        ↓
Cerrar o transferir
```
