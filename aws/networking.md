# AWS Networking

## IPv4

IPv4 addresses represent a 32-bit number.

IPv4 uses the dotted decimal notation to represent an address (eg 10.20.0.1).

## CIDR explination

10.0.0.0/24

Each of the numbers [10] [0] [0] [0] is an octet
Each octet represents 8 bits
Together 4 octets represent 32 bits

The last part of the CIDR notation is the number of bits that are frozen in place
In this case 24 bits are frozen in place
Note that this locked number has to be a multiple of 8

The multiples of 8 are 8, 16, 24, 32, 40, 48, 56, 64

So if the last part in the CIDR notation is /24 that means

- 32 - 24 = 8 bits are available for us to use

So only the last octet is available for us to use

Some example IP addresses that can be used in this range are

10.0.0.1
10.0.0.2
...

We can continue on in this way until we reach

10.0.0.255

This is the broadcast address and is not used as an address

So in this case we have 254 addresses available for our use

10.0.0.1 - 10.0.0.254

/24 last number = 10.0.0.1 - 10.0.0.254
/16 last two numbers = 10.0.0.1 - 10.0.255.254
/8 last three numbers = 10.0.0.1 - 10.255.255.254

Remember to calculate the number of addresses available in the cider block we use the formula

2<sup>32 - n</sup> - 2

where n is the number of bits frozen in place

So for a /24 we have

2<sup>32 - 24</sup> - 2 = 2<sup>8</sup> - 2 = 256 - 2 = 254

For a /16 we have

2<sup>32 - 16</sup> - 2 = 2<sup>16</sup> - 2 = 65,536 - 2 = 65,534

For a /8 we have

2<sup>32 - 8</sup> - 2 = 2<sup>24</sup> - 2 = 16,777,216 - 2 = 16,777,214

## Subnets

Subnetting is the process of dividing a network into smaller networks.

### The Math

- Each IPv4 address is made up of 4 octets or 4 sections of 8 bits.
- Each octet contains 2<sup>8</sup> = 256 possible values (0-255).
- Four octets means 256<sup>4</sup> = 4,294,967,296 possible values.

There are certain ranges that are reserved for specific uses.

0.0.0.0 is not used

typically addresses ending in .255 are not used as an address because they are used as broadcast addresses

for example 1.2.3.255 would not be used as an address



## IPv6 Addresses

IPv6 addresses represent a 128-bit number.

IPv6 uses hexadecimal notation to represent an address (eg 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

It has 8 segments of 16 bits each, separated by colons formatted in hexadecimal.

Addresses can be shorted by removing leading zeros and replacing consecutive zeros with a double colon.

For example, 2001:0db8:85a3:0000:0000:8a2e:0370:7334 can be shortened to 2001:db8:85a3::8a2e:370:7334.

Note: Consecutive zeros are replaced by a single double colon.

### The Math

- Each IPv6 address is made up of 8 sections of 16 bits.
- Each section contains 2<sup>16</sup> = 65,536 possible values (0-65535).
- Eight sections means 65,536<sup>8</sup> = 340,282,366,920,938,463,463,374,607,431,768,211,456 possible values.
- That's 340 undecillion, 282 decillion, 366 nonillion, 920 octillion, 938 septillion, 463 sextillion, 463 quintillion, 374 quadrillion, 607 trillion, 431 billion, 768 million, 211 thousand, 456 possible values.
- That's 340,282,366,920,938,463,463,374,607,431,768,211,456 possible values.
- That's 340 trillion, 282 billion, 366 million, 920 thousand, 938 possible values.
- That's 340 billion, 282 million, 366 thousand, 920 possible values.

## Classless Inter-Domain Routing (CIDR) Notation

### An Example

10.0.0.0/16 "CIDR notation"

the /16 is the "Leading bits"

That means the first 16 bits are the network address are frozen in place so this gives us a range
from

10.0.0.0 to 10.0.255.255

which amounts to 2<sup>16</sup> = 65,536 possible addresses

Not all of them will be usable

### Another Example

10.0.0.0/24

- this means the first 24 bits are frozen in place
- this leaves 32 - 24 = 8 bits for the available addresses
- 2<sup>8</sup> = 256 possible addresses


<table>
    <thead>
        <td>CIDR Block</td>
        <td>Number of Addresses</td>
        <td>Start Address</td>
        <td>End Address</td>
    </thead>
    <tbody>
        <tr>
            <td>10.0.0.0/8</td>
            <td>16,777,216</td>
            <td>10.0.0.0</td>
            <td>10.255.255.255</td>
        </tr>
        <tr>
            <td>10.0.0.0/16</td>
            <td>65,536</td>
            <td>10.0.0.0</td>
            <td>10.0.255.255</td>
        </tr>
        <tr>
            <td>10.0.0.0/17</td>
            <td>32,768</td>
            <td>10.0.0.0</td>
            <td>10.0.127.255</td>
        </tr>
        <tr>
            <td>10.0.0.0/18</td>
            <td>16,382</td>
            <td>10.0.0.0</td>
            <td>10.0.63.255</td>
        </tr>
        <tr>
            <td>10.0.0.0/28</td>
            <td>16</td>
            <td>10.0.0.0</td>
            <td>10.0.0.15</td>
        </tr>
    </tbody>
</table>

### Subnet Limitations
 
- When we create subnets the largest subnet we can create is /16 giving us 65,536 addresses. 
- The smallest subnet we can create is /28 giving us 16 addresses.


## Public Network Ranges

- can communicate directly with the internet

## Private Network Ranges

We have agreed that these ranges are private and will not be used on the internet.

<table>
    <thead>
        <td>CIDR Block</td>
        <td>Number of Addresses</td>
        <td>Start Address</td>
        <td>End Address</td>
    </thead>
    <tbody>
        <tr>
            <td>10.0.0.0/8</td>
            <td>16,777,216</td>
            <td>10.0.0.0</td>
            <td>10.255.255.255</td>
        </tr>
        <tr>
            <td>172.16.0.0/12</td>
            <td>1,048,576</td>
            <td>172.16.0.0</td>
            <td>172.31.255.255</td>
        </tr>
        <tr>
            <td>192.168.0.0/16</td>
            <td>65,536</td>
            <td>192.168.0.0</td>
            <td>192.168.255.255</td>
        </tr>
    </tbody>
</table>

When we create a VPC we will use one of these three addresses.

RFC1918 of Internet Engineering Task Force (IETF)

## Amazon Virtual Private Cloud (VPC)

We get logically isolated networks

They cannot communicate with each other unless we explicitly allow them to do so.

Default VPC per Account/Region

VPCs created per Account per Region

VPCs span a single Region

Can use all Availability Zones within one region

Can peer with other VPCs (connect VPCs together)

We can connect our VPC to the internet

We can connect our VPC to our on-premises network

We are limited to 5 VPCs per region

200 subnets per VPC


Note: If VPC's are created in the same region with overlapping CIDR blocks they cannot be peered.



## Creating VPCS

Before we can launch an EC2 instance we have to have a subnet

When we create a subnet we put it in an availability zone


10.2.0.0/24 in us-east-1a

10.2.1.0/24 in us-east-1b

10.2.2.0/28 in us-east-1c

when we create subnets Amazon VPC reserves the first 4 and last 1 IP

So for the subnet in us-east-1a we have

- 10.2.0.0
- 10.2.0.1 (VPC Router)
- 10.2.0.2
- 10.2.0.3
- 10.2.0.255 (Broadcast - Unused)

all reserved by Amazon VPC by default
So we have 251 IP addresses available for our use






## References

- [CIDR Calculator](https://www.subnet-calculator.com/cidr.php)
- [CIDR Block Application](https://cidr.xyz/)