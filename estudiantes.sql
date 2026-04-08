-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-03-2026 a las 15:33:47
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `notas2026`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `Edad` int(11) DEFAULT NULL,
  `Carrera` varchar(100) DEFAULT NULL,
  `nota1` decimal(3,2) DEFAULT NULL,
  `nota2` decimal(3,2) DEFAULT NULL,
  `nota3` decimal(3,2) DEFAULT NULL,
  `Promedio` decimal(3,2) DEFAULT NULL,
  `Desempeño` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `Nombre`, `Edad`, `Carrera`, `nota1`, `nota2`, `nota3`, `Promedio`, `Desempeño`) VALUES
(1, 'Paula', 21, 'Fisica', 4.00, 4.00, 3.00, 3.00, 'Bueno'),
(2, 'Ana', 18, 'Ingenieria', 2.00, 5.00, 3.00, 3.00, 'Regular'),
(3, 'Maria', 23, 'Ingenieria', 5.00, 4.00, 3.00, 4.00, 'Bueno'),
(4, 'Luis', 22, 'Matematicas', 2.00, 3.00, 4.00, 3.00, 'Regular'),
(5, 'Ana', 21, 'Ingenieria', 5.00, 5.00, 5.00, 5.00, 'Excelente'),
(6, 'Maria', 23, 'Ingenieria', 4.00, 3.00, 3.00, 3.00, 'Regular'),
(7, 'Ana', 20, 'Fisica', 2.00, 3.00, 3.00, 2.00, 'Regular'),
(8, 'Luis', 20, 'Ingenieria', 4.00, 2.00, 4.00, 3.00, 'Bueno'),
(9, 'Luis', 23, 'Fisica', 4.00, 3.00, 2.00, 3.00, 'Regular'),
(10, 'Luis', 22, 'Ingenieria', 3.00, 3.00, 2.00, 2.00, 'Regular'),
(11, 'Ana', 20, 'Fisica', 5.00, 3.00, 2.00, 3.00, 'Regular'),
(12, 'Carlos', 19, 'Fisica', 4.00, 2.00, 2.00, 2.00, 'Regular'),
(13, 'Luis', 21, 'Fisica', 2.00, 5.00, 5.00, 4.00, 'Bueno'),
(14, 'Maria', 22, 'Fisica', 5.00, 2.00, 2.00, 3.00, 'Regular'),
(15, 'Jose', 18, 'Fisica', 4.00, 3.00, 2.00, 3.00, 'Regular'),
(16, 'Paula', 21, 'Fisica', 5.00, 4.00, 2.00, 3.00, 'Bueno'),
(17, 'Luis', 22, 'Ingenieria', 2.00, 3.00, 2.00, 2.00, 'Deficiente'),
(18, 'Maria', 22, 'Matematicas', 5.00, 5.00, 2.00, 4.00, 'Bueno'),
(19, 'Luis', 20, 'Matematicas', 5.00, 4.00, 5.00, 4.00, 'Excelente'),
(20, 'Ana', 22, 'Ingenieria', 2.00, 3.00, 4.00, 3.00, 'Regular'),
(21, 'Ana', 20, 'Fisica', 3.00, 5.00, 2.00, 3.00, 'Bueno'),
(22, 'Carlos', 20, 'Ingenieria', 2.00, 4.00, 5.00, 3.00, 'Bueno'),
(23, 'Luis', 23, 'Fisica', 3.00, 2.00, 5.00, 3.00, 'Bueno'),
(24, 'Ana', 21, 'Ingenieria', 3.00, 5.00, 4.00, 4.00, 'Bueno'),
(25, 'Carlos', 19, 'Matematicas', 4.00, 3.00, 3.00, 3.00, 'Regular'),
(26, 'Maria', 18, 'Fisica', 3.00, 3.00, 5.00, 3.00, 'Bueno'),
(27, 'Carlos', 22, 'Matematicas', 3.00, 4.00, 2.00, 3.00, 'Regular'),
(28, 'Luis', 21, 'Ingenieria', 2.00, 3.00, 5.00, 3.00, 'Regular'),
(29, 'Jose', 20, 'Matematicas', 4.00, 3.00, 3.00, 3.00, 'Regular'),
(30, 'Ana', 19, 'Ingenieria', 3.00, 2.00, 3.00, 3.00, 'Regular'),
(31, 'Maria', 18, 'Ingenieria', 5.00, 4.00, 4.00, 4.00, 'Excelente'),
(32, 'Maria', 23, 'Fisica', 2.00, 3.00, 4.00, 3.00, 'Regular'),
(33, 'Jose', 18, 'Matematicas', 5.00, 3.00, 4.00, 4.00, 'Bueno'),
(34, 'Ana', 18, 'Matematicas', 5.00, 2.00, 5.00, 4.00, 'Bueno'),
(35, 'Jose', 20, 'Fisica', 2.00, 2.00, 2.00, 2.00, 'Deficiente'),
(36, 'Paula', 23, 'Fisica', 5.00, 5.00, 3.00, 4.00, 'Bueno'),
(37, 'Jose', 18, 'Fisica', 4.00, 3.00, 3.00, 3.00, 'Bueno'),
(38, 'Ana', 21, 'Fisica', 5.00, 3.00, 5.00, 4.00, 'Excelente'),
(39, 'Ana', 22, 'Ingenieria', 3.00, 5.00, 2.00, 3.00, 'Bueno'),
(40, 'Ana', 23, 'Fisica', 3.00, 2.00, 2.00, 2.00, 'Regular'),
(41, 'Luis', 18, 'Fisica', 3.00, 3.00, 4.00, 3.00, 'Bueno'),
(42, 'Luis', 23, 'Fisica', 3.00, 4.00, 3.00, 3.00, 'Bueno'),
(43, 'Ana', 22, 'Fisica', 2.00, 5.00, 3.00, 3.00, 'Regular'),
(44, 'Maria', 21, 'Fisica', 5.00, 5.00, 4.00, 4.00, 'Excelente'),
(45, 'Paula', 20, 'Matematicas', 2.00, 3.00, 2.00, 2.00, 'Deficiente'),
(46, 'Ana', 18, 'Fisica', 5.00, 2.00, 2.00, 3.00, 'Regular'),
(47, 'Felipe Tellez', 23, 'Ingenieria', 4.00, 4.00, 4.00, 4.00, 'Bueno'),
(48, 'Marcos', 18, 'Ingenieria', 5.00, 5.00, 5.00, 5.00, 'Excelente'),
(49, 'MarcosLobo', 25, 'Ingenieria', 5.00, 5.00, 5.00, 5.00, 'Excelente'),
(50, 'Lobo2', 36, 'Fisica', 5.00, 5.00, 5.00, 5.00, 'Excelente'),
(51, 'Lobo2_TEST', 20, 'Fisica', 3.00, 4.00, 5.00, 4.00, 'Bueno'),
(52, 'Vocero', 25, 'Ingenieria', 4.00, 1.00, 1.00, 2.00, 'Deficiente'),
(53, 'Sofia Torres', 20, 'Ingenieria', 4.50, 4.00, 5.00, 4.50, 'Excelente'),
(54, 'Diego Ramirez', 22, 'Fisica', 3.00, 2.50, 3.50, 3.00, 'Regular'),
(55, 'Valentina Ruiz', 19, 'Matematicas', 5.00, 5.00, 4.50, 4.83, 'Excelente'),
(56, 'Andres Mora', 23, 'Ingenieria', 2.00, 2.50, 3.00, 2.50, 'Deficiente'),
(57, 'Laura Perez', 21, 'Fisica', 4.00, 4.50, 4.00, 4.17, 'Bueno'),
(58, 'Maria Lopez', 35, 'Administracion Empresas', 4.45, 0.59, 3.08, 2.71, 'Bajo'),
(59, 'Valentina Mora', 28, 'Derecho', 0.57, 0.96, 3.05, 1.53, 'Bajo'),
(60, 'Andres Torres', 27, 'Derecho', 4.88, 0.72, 4.96, 3.52, 'Regular'),
(61, 'Valentina Mora', 24, 'Contaduria', 3.35, 3.14, 1.06, 2.52, 'Bajo'),
(62, 'Juan Perez', 24, 'Psicologia', 0.01, 3.05, 1.20, 1.42, 'Bajo'),
(63, 'Andres Torres', 30, 'Arquitectura', 0.43, 3.60, 1.53, 1.85, 'Bajo'),
(64, 'Sofia Herrera', 22, 'Medicina', 3.46, 1.29, 3.32, 2.69, 'Bajo'),
(65, 'Felipe Vargas', 23, 'Arquitectura', 1.41, 3.96, 0.49, 1.95, 'Bajo'),
(66, 'Felipe Vargas', 15, 'Administracion Empresas', 2.83, 0.78, 2.30, 1.97, 'Bajo'),
(67, 'Daniela Cruz', 13, 'Derecho', 0.92, 0.76, 3.50, 1.73, 'Bajo'),
(68, 'Jose Castro', 17, 'Medicina', 4.92, 0.81, 3.64, 3.12, 'Regular'),
(69, 'Ana Rodriguez', 17, 'Ingenieria Sistemas', 3.65, 3.31, 3.82, 3.59, 'Regular'),
(70, 'Laura Gutierrez', 21, 'Ingenieria Industrial', 1.58, 2.43, 0.81, 1.61, 'Bajo'),
(71, 'Daniela Cruz', 25, 'Administracion Empresas', 3.64, 4.99, 3.43, 4.02, 'Bueno'),
(72, 'Felipe Vargas', 27, 'Contaduria', 1.47, 3.38, 4.69, 3.18, 'Regular'),
(73, 'Valentina Mora', 0, 'Ingenieria Industrial', 4.03, 3.31, 4.91, 4.08, 'Bueno'),
(74, 'Maria Lopez', 17, 'Ingenieria Industrial', 4.29, 0.02, 1.73, 2.01, 'Bajo'),
(75, 'Luis Martinez', 15, 'Arquitectura', 1.34, 1.31, 3.42, 2.02, 'Bajo'),
(76, 'Laura Gutierrez', 24, 'Ingenieria Sistemas', 2.18, 3.00, 3.29, 2.82, 'Bajo'),
(77, 'Laura Gutierrez', 6, 'Psicologia', 3.83, 2.96, 0.46, 2.42, 'Bajo'),
(78, 'Sebastian Ruiz', 29, 'Ingenieria Industrial', 4.96, 1.59, 1.92, 2.82, 'Bajo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
